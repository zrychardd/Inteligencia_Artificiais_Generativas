# ==============================================================================
# EXERCÍCIO 6: Gerenciamento de Recursos com with Statement
# Enunciado: O código abaixo abre e fecha um arquivo manualmente, o que pode 
# levar a problemas se ocorrer uma exceção. Refatore-o para usar o with statement.
# ==============================================================================

# --- CÓDIGO ANTES DA REFATORAÇÃO ---
# def ler_arquivo_manual(nome_arquivo):
#     f = open(nome_arquivo, "r")
#     conteudo = f.read()
#     f.close()
#     return conteudo


# --- CÓDIGO DEPOIS DA REFATORAÇÃO ---
def ler_arquivo_manual(nome_arquivo):
    # O bloco 'with' funciona como um Context Manager que abre e fecha o arquivo
    with open(nome_arquivo, "r") as f:
        conteudo = f.read()
    
    return conteudo


# Preparação e Teste do Exercício 6
with open("teste.txt", "w") as f:
    f.write("Olá, mundo!")

print("Exercício 6:", ler_arquivo_manual("teste.txt"))

# --- O QUE MUDOU? ---
# 1. Segurança de Recursos: Se ocorrer um erro durante o 'f.read()', o bloco 'with' 
#    garante que o arquivo seja fechado no sistema operacional mesmo assim.
#
# 2. Código mais limpo: Não precisamos mais chamar explicitamente o 'f.close()', 
#    o próprio Python cuida do encerramento ao sair do escopo do bloco.
# ==============================================================================