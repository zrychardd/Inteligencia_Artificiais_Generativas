# ==============================================================================
# EXERCÍCIO 3: Refatoração para List Comprehension
# Enunciado: Refatore o código abaixo para usar uma list comprehension, 
# tornando-o mais conciso e legível.
# ==============================================================================

# --- CÓDIGO ANTES DA REFATORAÇÃO ---
# def filtra_e_dobra(numeros):
#     resultado = []
#     for num in numeros:
#         if num > 5:
#             resultado.append(num * 2)
#     return resultado


# --- CÓDIGO DEPOIS DA REFATORAÇÃO ---
def filtra_e_dobra(numeros):
    # Usando list comprehension para filtrar e transformar em uma única linha
    return [num * 2 for num in numeros if num > 5]


# Teste do Exercício 3
print("Exercício 3:", filtra_e_dobra([1, 6, 3, 8, 2, 10]))  # Esperado: [12, 16, 20]

# --- O QUE MUDOU? ---
# 1. Redução de Linhas: Toda a estrutura interna de criação de lista vazia,
#    loop 'for' e condição 'if' foi reduzida a apenas uma linha dentro do return.
#
# 2. Desempenho e Legibilidade: A sintaxe de List Comprehension é mais performática
#    em Python e segue a ordem natural do pensamento: [ação / laço / filtro].
# ==============================================================================