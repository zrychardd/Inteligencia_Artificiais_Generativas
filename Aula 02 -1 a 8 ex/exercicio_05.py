# ==============================================================================
# EXERCÍCIO 5: Refatoração com Cláusulas de Guarda (Guard Clauses)
# Enunciado: A função abaixo verifica várias condições aninhadas. Refatore-a 
# usando cláusulas de guarda para melhorar a legibilidade e reduzir a complexidade.
# ==============================================================================

# --- CÓDIGO ANTES DA REFATORAÇÃO ---
# def processar_pedido(status, quantidade, estoque):
#     if status == "aprovado":
#         if quantidade > 0:
#             if estoque >= quantidade:
#                 return "Pedido processado com sucesso!"
#             else:
#                 return "Erro: Estoque insuficiente."
#         else:
#             return "Erro: Quantidade inválida."
#     else:
#         return "Erro: Status do pedido não aprovado."


# --- CÓDIGO DEPOIS DA REFATORAÇÃO ---
def processar_pedido(status, quantidade, estoque):
    # Cláusula de guarda 1: Valida o status imediatamente
    if status != "aprovado":
        return "Erro: Status do pedido não aprovado."
    
    # Cláusula de guarda 2: Valida a quantidade imediatamente
    if quantidade <= 0:
        return "Erro: Quantidade inválida."
    
    # Cláusula de guarda 3: Valida o estoque imediatamente
    if estoque < quantidade:
        return "Erro: Estoque insuficiente."
    
    # Fluxo principal de sucesso (sem aninhamento)
    return "Pedido processado com sucesso!"


# Testes do Exercício 5
print("Exercício 5 - Sucesso:", processar_pedido("aprovado", 5, 10))
print("Exercício 5 - Erro 1:", processar_pedido("aprovado", 5, 3))
print("Exercício 5 - Erro 2:", processar_pedido("pendente", 5, 10))

# --- O QUE MUDOU? ---
# 1. Fim do "Efeito Pirâmide": Eliminamos os múltiplos 'if' aninhados que deixavam 
#    o código com recuos excessivos para a direita.
#
# 2. Falhe Rápido (Fail Fast): Validamos os erros primeiro e saímos da função logo 
#    no início. O caso de sucesso fica limpo na base do código, sem necessidade 
#    de usar blocos 'else'.
# ==============================================================================
