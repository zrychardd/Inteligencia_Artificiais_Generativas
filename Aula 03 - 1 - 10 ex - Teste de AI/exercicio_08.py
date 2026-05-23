"""
AULA 03 - Exercício 8: Detectando Limitações da IA (Teste de Estresse Lógico)

ENUNCIADO:
Peça algo incomum:
tema_historia = "uma bicicleta que viaja no tempo usando pizza como combustível"

Depois execute e responda no texto:
- A IA conseguiu criar sentido?
- A resposta ficou estranha ou coerente?

--------------------------------------------------------------------------------
ANÁLISE E RESPOSTAS DOS EXPERIMENTOS:

1. A IA conseguiu criar sentido?
R: Surpreendentemente, sim. A IA utilizou "lógica narrativa" para conectar as coisas. 
Em vez de tratar os elementos como erros, ela justificou o absurdo dentro do contexto 
da história: o queijo derretido virou o condutor de energia da corrente, o pepperoni 
virou o acelerador de partículas e o forno da pizzaria virou o portal temporal.

2. A resposta ficou estranha ou coerente?
R: Ficou coerente dentro do universo da fantasia (coerência interna). Embora a premissa 
seja completamente estranha e impossível no mundo real, o Gemini conseguiu manter a 
estrutura de começo, meio e fim, fazendo com que a história fizesse sentido para quem 
está lendo uma fábula ou um conto de ficção científica humorístico.

Conclusão: Grandes modelos de linguagem (LLMs) como o Gemini não travam diante de 
parodoxos ou absurdos; eles possuem uma capacidade avançada de associação semântica 
que encontra nexo causal até nas combinações mais aleatórias imaginadas pelo usuário.
--------------------------------------------------------------------------------
"""

from google import genai
from google.genai import types
from API import API  # Sua chave do Gemini que está neste arquivo

# Inicializa o cliente oficial da Google usando a sua chave
cliente = genai.Client(api_key=API)

# --- Parâmetros fixados do exercício anterior ---
personalidade = "Chef de cozinha francês"
idioma = "português do Brasil"
tamanho_resposta = "com no máximo 120 palavras"

# === MUDANÇA DO EXERCÍCIO 8 ===
# Testando o limite criativo e lógico do modelo com uma premissa absurda
tema_historia = "uma bicicleta que viaja no tempo usando pizza como combustível"

print(f"\nPreparando a história com a personalidade: {personalidade}")
print(f"Sobre o tema: {tema_historia}\n")

# Faz a requisição para o Gemini configurando o comportamento do modelo
resposta = cliente.models.generate_content(
    model='gemini-2.5-flash',
    contents=f"Escreva uma história de ninar {tamanho_resposta} sobre {tema_historia}.",
    config=types.GenerateContentConfig(
        system_instruction=f"Você é {personalidade}. Responda em {idioma}."
    )
)

print("--- Resposta da IA ---")
print(resposta.text)
print("---------------------\n")