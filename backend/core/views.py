from rest_framework import viewsets
from rest_framework.response import Response
import os  
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from .models import Company, Document, Signer
from .serializers import CompanySerializer, DocumentSerializer, SignerSerializer
from .services import ZapSignService

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class SignerViewSet(viewsets.ModelViewSet):
    queryset = Signer.objects.all()
    serializer_class = SignerSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        
        document = serializer.save()

        
        zap_token = "584bb990-f108-4938-aa56-1e0ff25af8748670f2da-8452-4bb9-a529-bfe181ca0c01"
        zap_service = ZapSignService(zap_token)
        
        try:
            
            response_data = zap_service.create_document(
                document.name, 
                document.pdf_url if hasattr(document, 'pdf_url') else "https://www.orimi.com/pdf-test.pdf", 
                "Signatário Teste", 
                "teste@email.com"
            )

            
            if response_data:
                document.token = response_data.get('token')
                document.open_id = response_data.get('open_id')
                document.status = response_data.get('status', 'pending')
                document.save()
                
        except Exception as e:
            print(f"Erro na integração ZapSign: {str(e)}")

        
        self._run_ai_analysis(document)

    def _run_ai_analysis(self, document):
        try:
            
            content_to_analyze = f"Documento: {document.name}. ID Externo: {document.external_id}"
            
            llm = ChatGoogleGenerativeAI(
                model="models/gemini-1.5-flash",
                google_api_key=os.environ.get("GOOGLE_API_KEY"), 
                temperature=0
            )
            
            
            prompt = PromptTemplate.from_template(
                "Analise o documento '{content}'. Forneça: 1) Um resumo conciso. "
                "2) Três insights principais. 3) Liste possíveis tópicos ou cláusulas faltantes."
            )
            
            chain = prompt | llm
            response = chain.invoke({"content": content_to_analyze})
            
        
            document.summary = response.content
            document.insights = "Análise de IA concluída com sucesso."
            document.save()
            
        except Exception as e:
            document.summary = f"Erro no processamento da IA: {str(e)}"
            document.save()