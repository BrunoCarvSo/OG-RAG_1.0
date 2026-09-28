import os
from dotenv import load_dotenv #Para ler o .env
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Defina sua chave de API
load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

# Inicializa o modelo
llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)

cadeia = llm | StrOutputParser()

pergunta = input("Digite sua pergunta: ")

# Faz uma chamada direta via LangChain
resposta = cadeia.invoke(pergunta)

# Acessa o primeiro item da lista [0] e depois o valor da chave 'text'
print(resposta)

