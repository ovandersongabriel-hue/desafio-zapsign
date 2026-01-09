from django.test import TestCase
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Company, Document

class DocumentAITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.company = Company.objects.create(name="Test Co", api_token="fake_token")

    def test_document_creation_with_ai_and_zapsign_flow(self):
        
        fake_file = SimpleUploadedFile(
            "contrato.txt", 
            b"Este e um contrato de teste para analise de IA.", 
            content_type="text/plain"
        )

        payload = {
            "name": "Contrato de Teste IA",
            "company": self.company.id,
            "file": fake_file, 
            "signers": [
                {"name": "Signatario Teste", "email": "teste@email.com"}
            ]
        }
        
        
        response = self.client.post('/api/documents/', payload, format='multipart')
        
        self.assertEqual(response.status_code, 201)
        
        doc = Document.objects.get(name="Contrato de Teste IA")
        
        
        doc.refresh_from_db() 
        
        self.assertIsNotNone(doc.summary)
        self.assertIsNotNone(doc.insights)
        self.assertTrue(len(doc.summary) > 0)
        
        print(f"\n[TESTE IA] Resumo gerado: {doc.summary}")
        print(f"[TESTE IA] Insights gerados: {doc.insights}")