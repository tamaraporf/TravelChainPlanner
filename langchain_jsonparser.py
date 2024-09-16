from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.globals import set_debug
from dotenv import load_dotenv
import os
from langchain_core.pydantic_v1 import Field, BaseModel

load_dotenv()
set_debug(True)

class Destino(BaseModel):
    cidade = Field("Cidade a visitar")
    motivo = Field("Motivo pelo qual é interessante visitar")
    restaurantes = Field("Restaurantes populares entre pessoas locais")
    locais = Field("Atividades e locais culturais")


llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY") ,
                 model="gpt-3.5-turbo",
                 temperature=0.5)

parseador = JsonOutputParser(pydantic_object=Destino)


modelo_cidade = PromptTemplate(
    template="""Sugira uma cidade dado interesse por {interesse}.
    {formatacao_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()},
)

modelo_restaurante = PromptTemplate(
    template= """Sugira restaurantes populares entre pessoas locais em {cidade}
    {modelo_cidade}""",
    input_variables=["cidade"],
    partial_variables={"modelo_cidade": parseador.get_format_instructions()}
)

modelo_cultural = PromptTemplate(
    template = """Sugira atividades e locais culturais em {cidade}
    {modelo_cidade}""",
    input_variables=["cidade"],
    partial_variables={"modelo_cidade": parseador.get_format_instructions()}

)

chain_cidade = modelo_cidade | llm | parseador
chain_restaurante = modelo_restaurante | llm | parseador
chain_cultural = modelo_cultural | llm | parseador

chain = chain_cidade | chain_restaurante | chain_cultural

result = chain.invoke({'interesse': 'praias'})

print(result)