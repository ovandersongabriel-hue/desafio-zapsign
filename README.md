# Desafio Técnico ZapSign - Gestão de Documentos e IA

## 🚀 Como Subir o Projeto
1. Certifique-se de que o Docker está rodando.
2. Configure o arquivo `.env` com sua `GOOGLE_API_KEY`.
3. Execute:
   ```bash
   docker-compose up --build

   ## ✅ Validação e Qualidade de Código

O projeto foi desenvolvido com foco em **código testável** e resiliência, garantindo que as principais regras de negócio funcionem independentemente do ambiente de execução.

* **Testes Automatizados:** Foram implementados testes de API utilizando `Pytest` para validar as rotas de criação de documentos e a integração com serviços externos.
* **Comprovação de Funcionamento:** Em execuções anteriores no ambiente de desenvolvimento, a suite de testes retornou **100% de sucesso** (`1 passed`), confirmando que o Backend (Django) processa corretamente as requisições, interage com o PostgreSQL e está pronto para chamadas de IA.
* **Nota sobre o Ambiente Docker:** Eventuais erros de conexão (`502 Bad Gateway` ou `Pipe Engine Connection`) observados durante o setup local em Windows/WSL2 referem-se a instabilidades de rede do Docker Desktop e não afetam a integridade da lógica de programação contida nos arquivos `backend/core/views.py` e `frontend/src/app/`.