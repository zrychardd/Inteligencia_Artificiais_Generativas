# ==============================================================================
# EXERCÍCIO 2: Correção de Erro de Lógica
# Enunciado: A função abaixo deveria somar todos os números pares de uma lista, 
# mas está com um erro de lógica. Use a IA para corrigir a lógica e explique 
# o problema original.
# ==============================================================================

# --- CÓDIGO ANTES DA REFATORAÇÃO ---
# def soma_pares(lista_numeros):
#     total = 0
#     for numero in lista_numeros:
#         if numero % 2 != 0:
#             total += numero
#         return total


# --- CÓDIGO DEPOIS DA REFATORAÇÃO ---
def soma_pares(lista_numeros):
    total = 0
    for numero in lista_numeros:
        # Alterado de '!= 0' para '== 0' para filtrar os números pares
        if numero % 2 == 0:
            total += numero
            
    # Movido para fora do bloco 'for' (ajuste de indentação) para garantir
    # que a lista inteira seja percorrida antes de retornar o resultado
    return total


# Teste do Exercício 2
print("Exercício 2:", soma_pares([1, 2, 3, 4, 5, 6]))  # Esperado: 12 (2+4+6)

# --- O QUE MUDOU? ---
# 1. Correção da Condicional (Operador Módulo): O operador '%' calcula o resto da 
#    divisão. Se o resto da divisão por 2 for igual a 0 (== 0), o número é par. O 
#    código anterior usava '!= 0', o que somava os ímpares (1 + 3 + 5 = 9)
#
# 2. Correção de Fluxo (Indentação do Return): No código original, o 'return' estava 
#    dentro do laço 'for'. Isso causava uma finalização prematura da função logo 
#    no primeiro elemento processado. Ao retirar o 'return' do escopo do 'for', a 
#    função agora aguarda a checagem de todos os itens antes de devolver o total.
# ==============================================================================
