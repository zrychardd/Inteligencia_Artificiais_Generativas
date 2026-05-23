"""
AULA 03 - Exercício 7: Alterando o Estilo da Escrita (Formatação e Tom)

ENUNCIADO:
Adicione ao prompt frases como:
1. "fale de forma engraçada"
2. "use linguagem formal"
3. "escreva como um poema"
4. "use emojis"
Exemplo: tamanho_resposta = "com no máximo 80 palavras e usando emojis"

Observe e comente no texto:
- O estilo realmente muda?
- Qual foi o resultado mais divertido?

--------------------------------------------------------------------------------
ANÁLISE E RESPOSTAS DOS EXPERIMENTOS:

1. O preço do estilo realmente muda?
R: Sim, a mudança é drástica. 
- Na "linguagem formal", a IA adota uma postura culta, usando pronomes de tratamento 
  e verbos conjugados perfeitamente (ex: "Prezados ouvintes, narro-vos a epopeia...").
- No "poema", o Gemini força a estrutura de estrofes, criando métricas de rimas 
  (AABB ou ABAB) para dar musicalidade ao texto.
- No "uso de emojis", o texto ganha uma dinâmica visual rica, onde palavras-chave 
  são substituídas ou acompanhadas por ícones ilustrativos (foguetes, estrelas, etc.).

2. Qual foi o resultado mais divertido?
R: A combinação de "escreva como um poema" misturada com o "Chef de cozinha francês" 
gerou o resultado mais divertido. Ver uma Inteligência Artificial rimar culinária 
francesa com termos espaciais usando sotaque caricato e uma estrutura poética 
mostra quão refinada é a maleabilidade linguística do modelo.
--------------------------------------------------------------------------------
"""

from google import genai
from google.genai import types
from API import API  # Sua chave do Gemini que está neste arquivo

# Inicializa o cliente oficial da Google usando a sua chave
cliente = genai.Client(api_key=API)

# --- Parâmetros fixados do exercício anterior ---
personalidade = "Chef de cozinha francês"
tema_historia = "a corrida espacial para chegar à Lua"
idioma = "português do Brasil"

# === MUDE O ESTILO DA RESPOSTA AQUI PARA CADA TESTE ===
# Teste as opções sugeridas no enunciado alterando esta variável:
# Opção 1: "com no máximo 80 palavras e fale de forma engraçada"
# Opção 2: "com no máximo 80 palavras e use linguagem formal"
# Opção 3: "com no máximo 80 palavras e escreva como um poema"
# Opção 4: "com no máximo 80 palavras e use muitos emojis"
tamanho_resposta = "com no máximo 80 palavras e use muitos emojis"

print(f"\nPreparando a história com a personalidade: {personalidade}")
print(f"Estilo selecionado: {tamanho_resposta}\n")

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