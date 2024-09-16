from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"


prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma familia com {numero_de_criancas} crianças, que gostam de {atividade}"
print(prompt)

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY") ,
                 model="gpt-3.5-turbo",
                 temperature=0.5)

resposta = llm.invoke(prompt)

print(resposta.content)