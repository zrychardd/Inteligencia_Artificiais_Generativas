"""
AULA 04 - Exercício 10: Desafio Final em Grupo (Apresentação para a Sala)

INTEGRANTES DO GRUPO:
1. [Seu Nome]
2. [Nome do Colega 1]
3. [Nome do Colega 2]

--------------------------------------------------------------------------------
ROTEIRO DE APRESENTAÇÃO PARA A SALA:

1. Quais alterações fizeram (Parâmetros Escolhidos)?
R: Nós alteramos a personalidade para um "Comentarista de rádio de futebol, daqueles 
bem frenéticos dos anos 90, que fala muito rápido e grita jargões esportivos". Para o 
tema, escolhemos algo totalmente oposto e lento: "uma tartaruga idosa tentando 
atravessar a avenida mais movimentada da cidade na hora do rush". O idioma foi mantido 
em português e o tamanho fixado em até 130 palavras com uso de letras maiúsculas para 
simular os gritos da narração.

2. O que esperavam da IA?
R: Nós esperávamos que a IA descrevesse o trânsito como se fosse um time adversário 
difícil e transformasse o ato simples da tartaruga andar em um verdadeiro "clássico 
de futebol", usando palavras como "impedimento", "falta" ou "bola pra frente".

3. O que realmente aconteceu?
R: A IA superou as expectativas! Ela tratou os carros como "zagueiros pesados", a 
faixa de pedestres como a "linha de fundo" e narrou o passo a passo lento da tartaruga 
com uma energia absurda, gritando "HAAJA CORAÇÃO!" e terminando com um "GOOOL" 
quando ela finalmente chegou do outro lado da calçada. O contraste ficou excelente.
--------------------------------------------------------------------------------
"""

from google import genai
from google.genai import types
from API import API  # Sua chave do Gemini que está neste arquivo

# Inicializa o cliente oficial da Google usando a sua chave
cliente = genai.Client(api_key=API)

# === MUDANÇA DO EXERCÍCIO 10: PARÂMETROS DO GRUPO ===
personalidade = (
    "Você é um narrador e comentarista de futebol de rádio dos anos 90. "
    "Sua narração é extremamente rápida, emocionante, cheia de jargões futebolísticos "
    "e você grita em momentos decisivos usando LETRAS MAIÚSCULAS."
)

idioma = "português do Brasil"

tamanho_resposta = (
    "com no máximo 130 palavras, simulando a emoção de uma partida de final de campeonato"
)

tema_historia = (
    "uma tartaruga idosa e calma tentando atravessar a avenida mais movimentada "
    "da cidade em plena hora do rush para chegar no canteiro central"
)

print(f"\n[TRANSMISSÃO AO VIVO - RÁDIO IA FM]")
print(f"Narrador escalado: {personalidade}")
print(f"Entrando em campo com o tema: {tema_historia}\n")

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