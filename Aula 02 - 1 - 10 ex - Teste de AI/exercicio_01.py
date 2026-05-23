"""
AULA 03 - Exercício 1: Mudando a Personalidade da IA

ENUNCIADO:
Altere a variável personalidade para:
1. um astronauta perdido em Marte
2. um professor maluco de ciências
3. um samurai sábio

Execute o código após cada alteração e observe e comente no texto:
- Como muda o jeito da história?
- A IA usa palavras diferentes?
- O humor muda?

--------------------------------------------------------------------------------
ANÁLISE E RESPOSTAS DOS EXPERIMENTOS:

1. Como muda o jeito da história?
R: O "jeito" mudou sutilmente na introdução de cada uma, mas todas mantiveram a 
estrutura de uma narrativa pirata. Isso aconteceu porque a variável 'tamanho_resposta' 
tinha uma ordem muito forte: "usando gírias de pirata". 
- O Astronauta seguiu a ordem de forma padrão.
- O Professor Maluco misturou as duas coisas, criando a fusão "jovem cientista pirata" 
  e se auto-referenciando como "O Professor aqui".
- O Samurai Sábio ignorou sua própria personalidade pacífica para focar totalmente no 
  personagem pirata ("Ahoy, marujo! Argh!").

2. A IA usa palavras diferentes?
R: Sim, houve variação no vocabulário específico (léxico). O Professor Maluco trouxe 
termos como "jovem cientista", "pergaminho antigo" e "galeão dos sonhos". O Samurai 
Sábio utilizou um vocabulário clássico de histórias de piratas como "doubloons", 
"butim de cair o queixo" e "porto seguro". O Astronauta usou termos mais simples de 
ninar ("pequeno bucaneiro").

3. O humor muda?
R: O humor mudou drasticamente no caso do Professor Maluco, que gerou um tom mais 
agitado, elétrico e caótico ("ufa!", "uhm,", "antes que o Barba Negra te pegue"). As 
personalidades do Astronauta e do Samurai geraram um humor mais brando e focado no 
conforto do sono ("durma, meu pequeno bucaneiro", "Que a noite seja seu porto seguro").

Conclusão: Quando o 'system_instruction' (personalidade) entra em conflito com o 
'contents' (gírias de pirata), a IA tenta misturar os dois conceitos ou prioriza o 
comando mais específico do usuário.
--------------------------------------------------------------------------------
"""

from google import genai
from google.genai import types
from API import API  # Sua chave do Gemini que está neste arquivo

# Inicializa o cliente oficial da Google usando a sua chave
cliente = genai.Client(api_key=API)

# --- Parâmetros que os alunos irão modificar ---
# Testado com: "um astronauta perdido em Marte", "um professor maluco de ciências", "um samurai sábio"
personalidade = "um samurai sábio"

idioma = "português do Brasil"

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