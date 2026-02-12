# ============================
# Transcrição de Áudio com Whisper
# ============================

# Instalação da biblioteca Whisper diretamente do repositório oficial
!pip install git+https://github.com/openai/whisper.git -q

import whisper

# Carrega o modelo Whisper
model = whisper.load_model("small")

# Transcreve o áudio gravado anteriormente
result = model.transcribe(record_file, fp16=False, language=language)

# Obtém o texto transcrito
transcription = result["text"]
print(transcription)

