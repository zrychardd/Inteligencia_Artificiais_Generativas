print("---------Lista de compras----------")

Compras = []

while True:

    print("1 - Adicionar item")
    print("2 - Listar itens")
    print("4 - Remover item")
    print("5 - Sair")
    print("-------------------------")
    print()

    opcao = input("Escolha uma das opções: ")
    print()

    if opcao == "1":
        item = input("Digite o nome do item: ")
        Compras.append(item)
        print()
        print(f"{item} adicionado à lista de compras.")
        print("-------------------------")

    elif opcao == "2":

        if not Compras:
            print()
            print("A lista de compras está vazia.")

        else:
            print()
            print("Itens na lista de compras:")
            print()
            for i, item in enumerate(Compras):
                print(f"{i}. {item}")
                print()

    elif opcao == "4":
        break
