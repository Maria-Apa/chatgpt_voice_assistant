#instalando e importando o whisper
!pip install git+https://github.com/openai/whisper.git -q

import whisper

# Selecione o modelo do Whisper que melhor atenda às suas necessidades:
model = whisper.load_model("small")

# Transcreve o audio gravado anteriormente.
result = model.transcribe(record_file, fp16=False, language=language)
transcription = result["text"]
print(transcription)

# Exemplo de saída: "Quem foi Michael Jackson?"
