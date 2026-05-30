from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

API_KEY = "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"

if not API_KEY:
    raise ValueError("Erro: A variável API_KEY não foi encontrada. Verifique se o arquivo .env está na raiz do projeto.")

agent = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ), instructions="""responda a perguntas frequentes sobre um tópico específico (ex: história do Python, regras de um esporte). O chatbot deve ser capaz de lidar com um conjunto predefinido de perguntas e respostas, e informar quando não souber a resposta.""",
    markdown=True
)
while True:
    entrada = input("Usuario: ")
    if entrada.lower()=="sair":
        print("Encerrando...")
        break
    agent.print_response(
        entrada,
        session_id="dev_session",
        stream=True
    )