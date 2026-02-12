# Importando para o Python

from record_audio import record
from transcribe_audio import transcribe_audio
from chatgpt_response import ask_chatgpt
from text_to_speech import tts

API_KEY = "SUA_CHAVE_AQUI"

# Fases do código

# 1. Grava o áudio/pergunta
print("Gravando...")
audio_file = record(5)

# 2. Transcreve o áudio
print("Transcrevendo...")
text = transcribe_audio(audio_file)
print("Você disse:", text)

# 3. Resposta pelo ChatGPT
print("Respondendo...")
reply = ask_chatgpt(text, API_KEY)
print("ChatGPT:", reply)

# 4. Transforma a resposta em áudio
print("Reproduzindo resposta...")
tts(reply)
