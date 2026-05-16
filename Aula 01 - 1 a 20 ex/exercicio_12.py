print("-------Acesso por senha-------")
print()

senha_correta = "2341"
senha = ""

while senha != senha_correta:
    print()
    senha = input("Digite a senha: ")

    if senha != senha_correta:
        print()
        print("Senha incorreta. Tente novamente.")
print()
print("Acesso permitido!")
print()