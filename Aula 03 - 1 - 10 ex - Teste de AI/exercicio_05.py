"""
AULA 03 - Exercício 5: Criando Novos Temas (Criatividade da IA)

ENUNCIADO:
Troque tema_historia por:
1. "um dragão vegetariano"
2. "uma cidade escondida no fundo do oceano"
3. "um computador que ganhou vida"

Analise e comente no texto:
- A criatividade da IA muda?
- Qual tema gerou a história mais interessante?

--------------------------------------------------------------------------------
ANÁLISE E RESPOSTAS DOS EXPERIMENTOS:

1. A criatividade da IA muda?
R: Sim, a criatividade se adapta drasticamente para se moldar ao tema. Quando 
o tema propõe uma quebra de expectativa (como o "dragão vegetariano"), a IA ativa 
um lado mais cômico e irônico. Em cenários de exploração ("cidade no fundo do oceano"), 
ela foca na construção de um ambiente visual rico e mágico. Já em temas tecnológicos 
("computador que ganhou vida"), ela brinca com metáforas do nosso cotidiano digital.

2. Qual tema gerou a história mais interessante?
R: O tema do "dragão vegetariano" gerou a narrativa mais interessante e divertida. 
A IA foi muito criativa ao criar o conflito do dragão que se recusava a queimar 
vilas e preferia usar seu fogo apenas para grelhar vegetais ou fazer churrasco de 
milho. A mistura dessa premissa com as "gírias de pirata" exigidas no prompt gerou 
um contraste hilário e único (um pirata contando a história de um dragão que ama brócolis).
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

tamanho_resposta = (
    "com no máximo 100 palavras"
)

# === MUDE O TEMA AQUI PARA CADA TESTE ===
# Opções: "um dragão vegetariano", "uma cidade escondida no fundo do oceano" ou "um computador que ganhou vida"
tema_historia = "uma cidade escondida no fundo do oceano"

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