from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Define variables
numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

# Define the prompt template and fill in the variables
template = PromptTemplate.from_template(
"Crie um roteiro de viagem de {dias} dias, para uma familia com {criancas} crianças, que gostam de {atividade}"
)

# Create the prompt with the filled-in variables
prompt= template.format(dias=numero_de_dias,
                criancas=numero_de_criancas,
                atividade=atividade)

# Create the LLM (Language Model)
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY") ,
                 model="gpt-3.5-turbo",
                 temperature=0.5)

# Use the LLM to generate the roteiro de viagem
report = llm.invoke(prompt)

# Print the generated report to the console
print(report.content)