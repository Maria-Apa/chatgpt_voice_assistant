# chatgpt_voice_assistant

## 🎯 Objetivo 

Este projeto foi desenvolvido para um bootcamp da DIO e tem como objetivo criar um sistema que combina as tecnologias de Speech-to-Text (voz para texto) e Text-to-Speech (texto para voz) para permitir uma conversa por voz, em múltiplos idiomas, com o ChatGPT.

Graças ao modelo Whisper, da OpenAI, é possível transcrever e traduzir sua fala com alta precisão. Em conjunto com o ChatGPT, o sistema entende sua pergunta e gera uma resposta inteligente. Para fechar o ciclo, utilizamos o Google Text-to-Speech (gTTS) para transformar a resposta em áudio.

O fluxo funciona assim:
1. Você fala algo no microfone
2. O Whisper transcreve sua fala
3. A transcrição é enviada ao ChatGPT
4. O ChatGPT gera a resposta
5. A resposta é convertida em áudio pelo gTTS
6. O sistema reproduz a resposta em voz

Tudo isso usando Python e bibliotecas modernas de IA.

## O que é o Whisper?

O Whisper é uma tecnologia de Reconhecimento Automático de Fala (ASR) criada pela OpenAI. <br>
Treinado com 680.000 horas de dados multilíngues coletados na web, ele oferece:

* Alta robustez a sotaques
* Boa resistência a ruídos de fundo
* Capacidade de entender termos técnicos
* Suporte a vários idiomas

Por isso, ele é ideal para aplicações que exigem transcrição confiável e interação por voz — como este projeto.

## 🚀 Tecnologias usadas

* Python 3.10+
* Google Colab
* Whisper (OpenAI)
* OpenAI Chat Completions API
* gTTS (Google Text-to-Speech)
* Torch
* NumPy

## 📝 Informações adicionais
Para verificar a documentação oficial da API da OpenAI, acesse: <br>
https://platform.openai.com/docs/api-reference/introduction

Para utilizar a OpenAI, é necessário ter uma versão paga. Caso prefira usar sem custos, consulte seu período gratuito: <br>
https://help.openai.com/en/articles/4936830

Para testar o projeto, você precisará gerar uma chave de API da OpenAI. Essa chave não deve ser compartilhada ou exposta publicamente, <br>
pois é uma informação sigilosa. <br>
No código, onde aparecer "SUA_CHAVE_AQUI", substitua pelo valor da sua chave real. <br>

Siga o passo a passo para localizar: 

1. Crie uma conta na OpenAI
2. Acesse a seção "API Keys"
3. Clique em "Create API Key" <br>

Link direto: https://platform.openai.com/account/api-keys

## 🛠️ Estrutura do projeto

Para facilitar a visualização do projeto, dividi o código em etapas separadas. Porém, para realizar os testes, basta adicionar tudo em uma única célula no Google Colab, que foi a ferramenta utilizada para executar esse projeto.

1. record_audio.py         → Captura o áudio do microfone <br>
2. transcribe_whisper.py   → Converte voz → texto com Whisper <br>
3.  chatgpt_response.py     → Envia a transcrição ao ChatGPT <br>
4.  tts_generate.py         → Texto → áudio usando gTTS <br>
5.  main.py                 → Orquestra todo o fluxo <br>

 
