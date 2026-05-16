# ==============================================================================
# EXERCÍCIO 1: Correção de Erro de Sintaxe
# Enunciado: O código abaixo contém um erro de sintaxe. Use a IA para 
# identificá-lo e corrigi-lo.
# ==============================================================================

# --- CÓDIGO ANTES DA REFATORAÇÃO ---
# def saudacao(nome)
#     print("Olá, " + nome + "!")
#
# saudacao("Mundo")


# --- CÓDIGO DEPOIS DA REFATORAÇÃO ---
def saudacao(nome):
    # Adicionados os dois-pontos (:) obrigatórios ao final da assinatura da função
    print("Olá, " + nome + "!")


# Teste do Exercício 1
saudacao("Mundo")

# --- O QUE MUDOU? ---
# 1. Correção do SyntaxError: Em Python, blocos de código estruturais (como funções 
#    'def', loops 'for'/'while' e condicionais 'if'/'elif'/'else') exigem 
#    obrigatoriamente o caractere de dois-pontos (:) ao final de sua declaração.
#
# 2. Definição do Escopo: Os dois-pontos servem para indicar ao interpretador do 
#    Python que a linha seguinte dará início a um bloco de código indentado.
# ==============================================================================
