# ==============================================================================
# EXERCÍCIO 7: Simplificação de Lógica Condicional Complexa
# Enunciado: A função abaixo possui uma série de if/elif/else que podem ser 
# simplificados, talvez usando um dicionário para mapear as ações.
# ==============================================================================

# --- CÓDIGO ANTES DA REFATORAÇÃO ---
# def obter_desconto(tipo_cliente, valor_compra):
#     if tipo_cliente == "premium":
#         if valor_compra > 1000:
#             return valor_compra * 0.20
#         else:
#             return valor_compra * 0.10
#     elif tipo_cliente == "gold":
#         if valor_compra > 500:
#             return valor_compra * 0.15
#         else:
#             return valor_compra * 0.05
#     else:
#         return 0


# --- CÓDIGO DEPOIS DA REFATORAÇÃO ---
def obter_desconto(tipo_cliente, valor_compra):
    # Mapeamento de regras: {tipo: (limite_valor, desconto_alto, desconto_baixo)}
    regras_desconto = {
        "premium": (1000, 0.20, 0.10),
        "gold": (500, 0.15, 0.05)
    }
    
    # Se o cliente não estiver mapeado (ex: "normal"), retorna 0 de desconto
    if tipo_cliente not in regras_desconto:
        return 0
        
    limite, desc_alto, desc_baixo = regras_desconto[tipo_cliente]
    
    # Operador ternário para escolher o percentual com base no valor da compra
    percentual = desc_alto if valor_compra > limite else desc_baixo
    
    return valor_compra * percentual


# Testes do Exercício 7
print("Exercício 7 - Premium:", obter_desconto("premium", 1200))  # 240.0
print("Exercício 7 - Gold:", obter_desconto("gold", 600))        # 90.0
print("Exercício 7 - Normal:", obter_desconto("normal", 200))    # 0

# --- O QUE MUDOU? ---
# 1. Separação de Dados e Lógica: As regras de negócio ficam centralizadas em uma 
#    estrutura de dados (dicionário), limpando a árvore de decisões.
#
# 2. Extensibilidade (Princípio Aberto/Fechado): Para adicionar um novo tipo de 
#    cliente (como "silver"), basta adicionar uma linha ao dicionário, sem alterar 
#    as condicionais da função.
# ==============================================================================