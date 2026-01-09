# Desafio Técnico ZapSign - Gestão de Documentos e IA

## 🚀 Como Subir o Projeto

1. **Certifique-se de que o Docker está rodando.**
2. **Configure as variáveis de ambiente:**
   - O projeto utiliza um arquivo `.env` para gerenciar chaves sensíveis.
   - Existe um modelo disponível em `.env.example`. Para configurar, você deve duplicá-lo:
     ```bash
     cp .env.example .env
     ```
   - Abra o arquivo `.env` e insira sua `GOOGLE_API_KEY` real.
3. **Execute o Docker Compose:**
   ```bash
   docker-compose up --build