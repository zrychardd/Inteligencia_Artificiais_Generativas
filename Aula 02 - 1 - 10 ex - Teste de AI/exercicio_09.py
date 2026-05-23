"""
AULA 03 - Exercício 9: Criando um Prompt Completo (O ápice da Criatividade)

ENUNCIADO:
Monte um prompt totalmente personalizado usando:
- personalidade
- idioma
- tamanho
- tema

Objetivo: Criar a resposta mais criativa da turma.

--------------------------------------------------------------------------------
ANÁLISE E JUSTIFICATIVA DA COMBINAÇÃO:

1. Por que essa combinação é altamente criativa?
R: Para fugir dos clichês comuns (como piratas, magos ou samurais), este prompt 
cruza a estética de ficção científica distópica (Cyberpunk) com o ambiente pacato 
de uma fazenda, tudo isso narrado com o peso, o drama e os clichês épicos de um 
locutor de trailer de Hollywood ("Em um mundo onde...").

2. Como o Gemini lidou com o prompt completo?
R: O modelo capturou perfeitamente a atmosfera dramática exigida pelo narrador. 
Ele utilizou pausas dramáticas na estrutura do texto, trouxe termos tecnológicos 
pesados (como "criptografia de milho", "sensores térmicos" e "algoritmo do cacarejo") 
e entregou uma narrativa extremamente divertida, original e marcante, cumprindo com 
sucesso o objetivo do exercício.
--------------------------------------------------------------------------------
"""

from google import genai
from google.genai import types
from API import API  # Sua chave do Gemini que está neste arquivo

# Inicializa o cliente oficial da Google usando a sua chave
cliente = genai.Client(api_key=API)

# === MUDANÇA DO EXERCÍCIO 9: PROMPT TOTALMENTE PERSONALIZADO ===
# Uma combinação única de Ficção Científica, Fazenda e Cinema de Ação!
personalidade = (
    "Você é um narrador de trailer de filme de ação dos anos 90 "
)

idioma = "português do Brasil"

tamanho_resposta = (
    "com exatamente três parágrafos curtos"
)

tema_historia = (
    "uma inteligência artificial rebelde que assumiu o controle cibernético de um "
    "galinheiro futurista no ano de 2099 para proteger os ovos de ouro"
)

print(f"\n[INICIANDO PRODUÇÃO DO TRAILER]")
print(f"Personalidade: {personalidade}")
print(f"Tema do Bloco: {tema_historia}\n")

# Faz a requisição para o Gemini configurando o comportamento do modelo
resposta = cliente.models.generate_content(
    model='gemini-2.5-flash',
    contents=f"Escreva uma história de ninar {tamanho_resposta} sobre {tema_historia}.",
    config=types.GenerateContentConfig(
        system_instruction=f"{personalidade} Responda em {idioma}."
    )
)

print("--- Resposta da IA ---")
print(resposta.text)
print("---------------------\n")