"""
AULA 03 - Exercício 2: Testando Idiomas da IA

ENUNCIADO:
Modifique a variável idioma para:
1. inglês
2. espanhol
3. francês

Depois, execute e comente no texto:
- Verifique se a resposta realmente mudou de idioma.
- Identifique palavras parecidas com o português.

--------------------------------------------------------------------------------
ANÁLISE E RESPOSTAS DOS EXPERIMENTOS:

1. Verifique se a resposta realmente mudou de idioma:
R: Sim, a IA realizou a tradução completa para cada um dos três idiomas solicitados. 
O ponto mais interessante é que ela conseguiu adaptar os termos e expressões náuticas/piratas 
para os equivalentes culturais de cada língua (como "Ahoy", "Matey" ou "Bucanero"), 
em vez de fazer apenas uma tradução literal palavra por palavra.
--------------------
"""

from google import genai
from google.genai import types
from API import API  # Sua chave do Gemini que está neste arquivo

# Inicializa o cliente oficial da Google usando a sua chave
cliente = genai.Client(api_key=API)

# --- Parâmetros que os alunos irão modificar ---
personalidade = "um samurai sábio"

# === MUDE O IDIOMA AQUI PARA CADA TESTE ===
# Opções: "inglês", "espanhol", "francês"
idioma = "francês"

tamanho_resposta = (
    "com no máximo 100 palavras, usando gírias de pirata"
)

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