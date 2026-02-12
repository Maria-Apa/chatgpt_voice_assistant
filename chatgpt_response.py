# instalando biblioteca
!pip install openai

import os
os.environ['OPENAI_API_KEY'] = 'SUA CHAVE'

import openai

# Configura a chave de API da OpenAI usando a variável de ambiente 'OPENAI_API_KEY'
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Envia uma requisição à API do ChatCompletion usando o modelo GPT-3.5 Turbo
# Lembrando que, a variável 'transcription' contém a transcrição do áudio.
response = openai.ChatCompletion.create(
    model="3.5 Turbo",
    messages=[ { "role": "user", "content": transcription } ]
)

# Obtém a resposta gerada pelo ChatGPT
chatgpt_response = response.choices[0].message.content
print(chatgpt_response)
