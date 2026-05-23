"""
AULA 03 - Exercício 6: Misturando Personagem e Tema (Conflito de Contextos)

ENUNCIADO:
Crie combinações diferentes:
1. Personalidade: Chef de cozinha francês  | Tema: corrida espacial
2. Personalidade: Detetive particular      | Tema: castelo assombrado
3. Personalidade: Robô engraçado          | Tema: floresta mágica

Objetivo: Descobrir como diferentes contextos alteram o resultado.

--------------------------------------------------------------------------------
ANÁLISE E RESPOSTAS DOS EXPERIMENTOS:

1. Como os diferentes contextos alteraram o resultado?
R: Os contextos alteram completamente o vocabulário básico e o foco da história. 
A IA cria pontes criativas (metáforas) para misturar a personalidade e o tema. 
- Na combinação 1 (Chef + Corrida Espacial), a IA transforma planetas em "suflês" 
  e o lançamento de um foguete em uma "receita com ponto de fervura perfeito".
- Na combinação 2 (Detetive + Castelo), o tom fica misterioso, focado em "pistas", 
  "pegadas de fantasmas" e "investigação de ruídos".
- Na combinação 3 (Robô + Floresta), o contraste entre tecnologia e natureza gera 
  piadas sobre "baterias descarregando por causa de feitiços" ou "fadas dando curto-circuito".

Conclusão: O Gemini mostra uma flexibilidade incrível. Ele não apenas escreve sobre 
o tema, mas reescreve o tema *através dos olhos* da personalidade escolhida, 
gerando resultados únicos para cada combinação.
--------------------------------------------------------------------------------
"""

from google import genai
from google.genai import types
from API import API  # Sua chave do Gemini que está neste arquivo

# Inicializa o cliente oficial da Google usando a sua chave
cliente = genai.Client(api_key=API)

# === MUDANÇA DO EXERCÍCIO 6 ===
# Altere as duas variáveis abaixo para testar as 3 combinações:
# Combinação 1: "Chef de cozinha francês" e "a corrida espacial para chegar à Lua"
# Combinação 2: "Detetive particular durão de filmes antigos" e "um mistério em um castelo assombrado"
# Combinação 3: "Robô engraçado e atrapalhado" e "uma jornada por uma floresta mágica"

personalidade = "Chef de cozinha francês"
tema_historia = "a corrida espacial para chegar à Lua"

idioma = "português do Brasil"
tamanho_resposta = "com no máximo 120 palavras"

print(f"\nPreparando a história com a personalidade: {personalidade}")
print(f"No idioma: {idioma}")
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