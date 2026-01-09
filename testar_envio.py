import json
import urllib.request
import urllib.error


url = "http://localhost:8000/api/documents/"  
dados = {
    "name": "Documento 004",
    "token": "token_teste_004",  
}


cabecalhos = {'Content-Type': 'application/json'}
dados_json = json.dumps(dados).encode('utf-8')
requisicao = urllib.request.Request(url, data=dados_json, headers=cabecalhos, method='POST')

print(f"Tentando enviar para: {url}")
print("-" * 30)

try:
    with urllib.request.urlopen(requisicao) as resposta:
        codigo = resposta.getcode()
        conteudo = resposta.read().decode('utf-8')
        
        if codigo == 201:
            print(f"✅ SUCESSO! Código: {codigo}")
            print("\nResposta da IA (Resumo):")
            print(conteudo)
        else:
            print(f"⚠️ Resposta inesperada: {codigo}")
            print(conteudo)

except urllib.error.HTTPError as e:
    print(f"❌ Erro HTTP: {e.code}")
    print(e.read().decode('utf-8'))
except urllib.error.URLError as e:
    print(f"❌ Erro de Conexão: {e.reason}")
    print("Dica: Verifique se o Docker está rodando e se a porta é 8000.")
except Exception as e:
    print(f"❌ Erro genérico: {e}")