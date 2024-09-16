from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.globals import set_debug
from dotenv import load_dotenv
import os

from langchain_simples import prompt

# Load environment variables from .env file
load_dotenv()

# Set debugging to get more detailed output from LangChain
set_debug(True)

# Create the LLM (Language Model)
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY") ,
                 model="gpt-3.5-turbo",
                 temperature=0.5)

# Define variables
modelo_cidade = ChatPromptTemplate.from_template(
    "Sugira uma cidade dado meu interesse por {interesse}"
)

modelo_restaurante = ChatPromptTemplate.from_template(
    "Sugira um restaurante populares entre pessoas locais em {cidade}"
)

modelo_cultural = ChatPromptTemplate.from_template(
    "Sugira atividades e locais culturais em {cidade}"
)


# Create the chains
cadeia_cidade = LLMChain(prompt=modelo_cidade, llm=llm)
cadeia_restaurante = LLMChain(prompt=modelo_restaurante, llm=llm)
cadeia_cultural = LLMChain(prompt=modelo_cultural, llm=llm)


# Create the main chain with all the chains together
cadeia = SimpleSequentialChain(chains=[cadeia_cidade,cadeia_restaurante,cadeia_cultural],
                               verbose=True)


# Set the interests
result = cadeia.invoke("praias")
print(result)
