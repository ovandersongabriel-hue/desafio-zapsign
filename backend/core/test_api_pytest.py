import pytest
from rest_framework import status
from core.models import Document, Company

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def company_instance(db):
    """Cria uma empresa com o seu token real da ZapSign"""
    return Company.objects.create(
        name="Empresa de Teste Integrado", 
        api_token="584bb990-f108-4938-aa56-1e0ff25af8748670f2da-8452-4bb9-a529-bfe181ca0c01" 
    )

@pytest.mark.django_db
class TestDocumentAPI:
    def test_create_document_success(self, api_client, company_instance):
        url = '/api/documents/'
        
        
        data = {
            "name": "Contrato de Teste Real",
            "company": company_instance.id,
            "external_id": "TEST-123",
            "token": "doc_unico_1001" 
        }
        
        response = api_client.post(url, data, format='json')
        
        
        if response.status_code != 201:
            print(f"\nResposta de Erro da API: {response.data}")
            
        assert response.status_code == status.HTTP_201_CREATED
        assert Document.objects.filter(name="Contrato de Teste Real").exists()