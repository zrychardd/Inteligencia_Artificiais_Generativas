# ==============================================================================
# EXERCÍCIO 4: Refatoração de Código Repetitivo
# Enunciado: O código abaixo contém repetição. Refatore-o para usar uma função 
# auxiliar ou outra estrutura que reduza a duplicação.
# ==============================================================================

# --- CÓDIGO ANTES DA REFATORAÇÃO ---
# def processa_dados_a(dados):
#     return [x * 2 for x in dados]
#
# def processa_dados_b(dados):
#     return [x + 10 for x in dados]
#
# def processa_dados_c(dados):
#     return [x - 5 for x in dados]


# --- CÓDIGO DEPOIS DA REFATORAÇÃO ---
def processa_dados(dados, operacao):
    # Uma única função genérica que recebe a lista e uma função de cálculo (operação)
    return [operacao(x) for x in dados]


# Dados de teste
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = [7, 8, 9]

# Teste do Exercício 4 usando funções lambda dinâmicas
print("Exercício 4 - A:", processa_dados(lista_a, lambda x: x * 2))
print("Exercício 4 - B:", processa_dados(lista_b, lambda x: x + 10))
print("Exercício 4 - C:", processa_dados(lista_c, lambda x: x - 5))

# --- O QUE MUDOU? ---
# 1. Aplicação do princípio DRY (Don't Repeat Yourself): Eliminamos três funções 
#    quase idênticas e criamos uma única função reaproveitável.
#
# 2. Injeção de Comportamento: Agora a função recebe um parâmetro chamado 'operacao' 
#    (uma função lambda), tornando o código escalável. Se novas operações surgirem, 
#    não precisamos criar novas funções.
# ==============================================================================