"""
AULA 03 - Exercício 3: Resposta Super Curta (Restrição de Tamanho)

ENUNCIADO:
Altere tamanho_resposta para:
1. "em uma única frase"
2. "com no máximo 15 palavras"

Observe e comente no texto:
- A IA consegue resumir bem?
- Ela mantém o tema mesmo com pouco espaço?

--------------------------------------------------------------------------------
ANÁLISE E RESPOSTAS DOS EXPERIMENTOS:

1. A IA consegue resumir bem?
R: Sim, o Gemini lida muito bem com resumos e obedece de forma rígida os limites 
impostos. No teste de "uma única frase", ele cria um período longo, porém contínuo. 
No teste de "no máximo 15 palavras", ele corta adjetivos desnecessários e foca 
apenas no núcleo da ação para não estourar a contagem.

2. Ela mantém o tema mesmo com pouco espaço?
R: Com certeza. Mesmo restrita a pouquíssimas palavras, os elementos essenciais 
solicitados ("mapa misterioso" e "tesouro") continuam aparecendo na resposta. 
A IA abre mão de detalhes secundários (como descrições da ilha ou gírias longas), 
mas preserva a ideia central da história perfeitamente.

Conclusão: Modelos como o 'gemini-2.5-flash' são excelentes para tarefas de 
compressão de texto e criação de manchetes, títulos ou notificações devido ao 
seu forte alinhamento com instruções de tamanho.
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
# Opções: "em uma única frase" ou "com no máximo 15 palavras"
tamanho_resposta = "com no máximo 35 palavras"

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