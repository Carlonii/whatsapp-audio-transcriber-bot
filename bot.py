from twilio.rest import Client
from flask import Flask, request, jsonify
from openai import OpenAI
import requests
from pydub import AudioSegment
from requests.auth import HTTPBasicAuth

OPENAI_API_KEY='sua_chave_api_aqui'
account_sid='seu_account_sid_aqui'
auth_token='seu_auth_token_aqui'

client = OpenAI()

app = Flask(__name__)

# Configurações do Twilio
twilio_client = Client(account_sid, auth_token)

def execute_script(question):
    response = f"{question}"
    return response

def convert_audio(input_file, output_file):
    # Converte o arquivo de áudio de ogg para wav
    audio = AudioSegment.from_file(input_file, format="ogg")
    audio.export(output_file, format="wav")

def transcribe_audio(file_path):
    with open(file_path, 'rb') as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

@app.route('/whatsapp', methods=['POST'])
def whatsapp_bot():
    audio_url = request.values.get('MediaUrl0')
    incoming_msg = ""

    if audio_url:
        print(f"URL do áudio recebido: {audio_url}")
        try:
            # Adicionando autenticação básica para acessar a URL
            response = requests.get(audio_url, auth=HTTPBasicAuth(account_sid, auth_token))
            print(f"Código de status do download do áudio: {response.status_code}")
            if response.status_code == 200:
                audio_content = response.content
                print(f"Tamanho do arquivo de áudio: {len(audio_content)} bytes")
                with open('audio_received.ogg', 'wb') as f:
                    f.write(audio_content)
                try:
                    convert_audio('audio_received.ogg', 'audio_received.wav')
                    incoming_msg = transcribe_audio('audio_received.wav')
                except Exception as e:
                    print(f"Erro na conversão ou transcrição: {e}")
                    incoming_msg = "Erro ao processar o áudio."
            else:
                incoming_msg = f"Erro no download do áudio. Status: {response.status_code}"
        except Exception as e:
            print(f"Erro ao tentar baixar o áudio: {e}")
            incoming_msg = "Erro no download do áudio."
    else:
        incoming_msg = request.values.get('Body', '').lower()

    from_number = request.values.get('From') 
    response = execute_script(incoming_msg)

    message = twilio_client.messages.create(
        body=response,
        from_='whatsapp:+14155238886',  # Número do WhatsApp da Twilio
        to=from_number
    )
    return str(message.sid)

if __name__ == '__main__':
    app.run(debug=True)
