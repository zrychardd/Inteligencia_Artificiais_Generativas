"""
AULA 03 - Exercício 4: História Longa (Expansão de Conteúdo)

ENUNCIADO:
Configure tamanho_resposta para:
1. "em três parágrafos"
2. "com no máximo 150 palavras"

Depois compare com as respostas curtas e comente no texto:
- O que mudou?
- A história ficou mais detalhada?

--------------------------------------------------------------------------------
ANÁLISE E RESPOSTAS DOS EXPERIMENTOS:

1. O que mudou?
R: Mudou completamente a estrutura e o ritmo da narrativa. Com o espaço estendido 
(especialmente na opção de "três parágrafos"), a IA dividiu a história com um arco 
clássico: Introdução (descoberta do mapa), Desenvolvimento (a jornada e os perigos 
no mar) e Conclusão (o encontro do tesouro e o momento de dormir). Nas versões 
curtas, tudo precisava acontecer ao mesmo tempo em uma linha só.

2. A história ficou mais detalhada?
R: Com certeza. A IA aproveitou o espaço extra para adicionar elementos descritivos 
que dão cor à história. Surgiram detalhes sobre o clima ("noite estrelada", "mar calmo"), 
características físicas do cenário ("palmeira torta", "areias prateadas") e ações 
secundárias dos personagens (como "abrir o baú com cuidado" ou "repartir o ouro"). 
A versão de 150 palavras alcança o equilíbrio ideal entre detalhes e a proposta de 
ser uma história de ninar rápida.
--------------------------------------------------------------------------------
"""

from google import genai
from google.genai import types
from API import API  # Sua chave do Gemini que está neste arquivo

# Inicializa o cliente oficial da Google usando a sua chave
cliente = genai.Client(api_key=API)

# --- Parâmetros que os alunos irão modificar ---
personalidade = "um samurai sábio"

idioma = "português do Brasil"

# === MUDE O TAMANHO DA RESPOSTA AQUI PARA CADA TESTE ===
# Opções: "em três parágrafos" ou "com no máximo 150 palavras"
tamanho_resposta = "com no máximo 150 palavras"

tema_historia = (
    "um mapa misterioso que leva a um tesouro "
)

print(f"\nPreparando a história com a personalidade: {personalidade}")
print(f"No idioma: {idioma}")
print(f"Sobre o tema: {tema_historia}\n")

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