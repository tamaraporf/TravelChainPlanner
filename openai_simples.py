from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"


prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma familia com {numero_de_criancas} crianças, que gostam de {atividade}"
# print(prompt)

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY") )

resposta = cliente.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Your are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

roteiro_viagem = resposta.choices[0].message.content
print(roteiro_viagem)

