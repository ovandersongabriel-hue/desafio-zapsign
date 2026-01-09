import requests

class ZapSignService:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://sandbox.api.zapsign.com.br/api/v1/docs/"

    def create_document(self, name, pdf_url, signer_name, signer_email):
        payload = {
            "name": name,
            "url_pdf": pdf_url,
            "signers": [{"name": signer_name, "email": signer_email}]
        }
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        response = requests.post(self.base_url, params={"api_token": self.api_token}, json=payload, headers=headers)
        return response.json()

class AIService:
    def __init__(self):
        self.api_token = "COLE_SEU_TOKEN_DA_HUGGING_FACE_AQUI"
        self.api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}

    def analisar_documento(self, texto):
        if not texto:
            return "Sem conteúdo para resumo", "Nenhum tópico identificado"
        
        payload = {"inputs": texto, "parameters": {"do_sample": False}}
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            resultado = response.json()
            summary = resultado[0].get('summary_text', 'Resumo não gerado') if isinstance(resultado, list) else "Erro na análise"
            insights = "Verificar cláusulas de rescisão e foro padrão"
            return summary, insights
        except Exception:
            return "Falha na comunicação com IA", "Tópicos indisponíveis"