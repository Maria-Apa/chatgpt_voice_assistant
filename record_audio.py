# ============================
#  Captura de Áudio no Colab
# ============================

# Define a língua principal usada na transcrição
language = 'pt'

# Importações necessárias 
from IPython.display import Audio, display, Javascript
from google.colab import output
from base64 import b64decode

# JavaScript que acessa o microfone e grava o áudio usando "MediaStream Recording API"
RECORD = """
const sleep  = time => new Promise(resolve => setTimeout(resolve, time))
const b2text = blob => new Promise(resolve => {
  const reader = new FileReader()
  reader.onloadend = e => resolve(e.srcElement.result)
  reader.readAsDataURL(blob)
})
var record = time => new Promise(async resolve => {
  stream = await navigator.mediaDevices.getUserMedia({ audio: true })
  recorder = new MediaRecorder(stream)
  chunks = []
  recorder.ondataavailable = e => chunks.push(e.data)
  recorder.start()
  await sleep(time)
  recorder.onstop = async ()=>{
    blob = new Blob(chunks)
    text = await b2text(blob)
    resolve(text)
  }
  recorder.stop()
})
"""

def record(sec=5):
# Grava áudio via navegador usando JavaScript e salva como WAV.
# Retorna o caminho do arquivo gerado.
  # Executa o código JS no Colab para iniciar a gravação
  display(Javascript(RECORD))
  
  # Recebe o áudio gravado em base64
  js_result = output.eval_js('record(%s)' % (sec * 1000))

  # Converte de base64 para bytes
  audio = b64decode(js_result.split(',')[1])

  # Salva o áudio como arquivo WAV
  file_name = 'request_audio.wav'
  with open(file_name, 'wb') as f:
    f.write(audio)
  return f'/content/{file_name}'

# ============================
# Gravar e Exibir Áudio
# ============================

print('Ouvindo...\n')
record_file = record()

# Exibe o áudio gravado
display(Audio(record_file, autoplay=False))
