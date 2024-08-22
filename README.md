# WhatsApp Audio Transcriber Bot

Este repositório contém um bot de WhatsApp que transcreve áudios enviados pelos usuários. O bot usa a API da OpenAI para transcrever o áudio e o Twilio para enviar e receber mensagens no WhatsApp.

## Funcionalidades

- Recebe mensagens de texto e áudios via WhatsApp.
- Transcreve áudios enviados em formato `ogg` para texto usando o modelo Whisper da OpenAI.
- Responde automaticamente com o texto transcrito ou com a mensagem de texto recebida.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **Flask**: Framework web utilizado para criar o servidor que gerencia as requisições do WhatsApp.
- **Twilio**: Plataforma utilizada para enviar e receber mensagens no WhatsApp.
- **OpenAI**: Utilizado para transcrever áudios via API.
- **Pydub**: Biblioteca utilizada para converter arquivos de áudio de `ogg` para `wav`.

## Instalação

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/Carlonii/whatsapp-audio-transcriber-bot
    cd whatsapp-audio-transcriber-bot
    ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use: venv\Scripts\activate
    ```

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure suas chaves de API**:
    - Renomeie o arquivo `.env.example` para `.env` e adicione suas chaves de API:
    ```bash
    cp .env.example .env
    ```

    - Preencha o arquivo `.env` com as seguintes informações:
    ```bash
    OPENAI_API_KEY='sua_chave_api_aqui'
    TWILIO_ACCOUNT_SID='seu_account_sid_aqui'
    TWILIO_AUTH_TOKEN='seu_auth_token_aqui'
    ```

5. **Execute o bot**:
    ```bash
    python app.py
    ```

## Uso

- Envie uma mensagem de texto ou áudio para o número do WhatsApp configurado no Twilio.
- O bot responderá com o texto transcrito se for um áudio, ou ecoará a mensagem de texto recebida.

## Estrutura do Código

- **bot.py**: O arquivo principal que contém a lógica do bot.
- **requirements.txt**: Arquivo contendo todas as dependências do projeto.

## Considerações de Segurança

- **NUNCA** compartilhe suas chaves de API publicamente. Use variáveis de ambiente para armazená-las de forma segura.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

