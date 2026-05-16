print("-----calculadora simples-----")

num1 = float(input("Diigite o primeiro número: "))
print()
num2 = float(input("Digite o segundo número: "))
print()


while True:
    print("-------------------------")
    print("1 - adição")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - Sair")
    print()



    opcao = int(input("Digite o número da operação: "))

    match opcao:
        case 1:
            resultado = num1 + num2
            print(f"O resultado da adição é: {resultado}")
        case 2:
            resultado = num1 - num2
            print(f"O resultado da subtração é: {resultado}")
        case 3:
            resultado = num1 * num2
            print(f"O resultado da multiplicação é: {resultado}")
        case 4:
            if num2 != 0:
                resultado = num1 / num2
                print(f"O resultado da divisão é: {resultado:.2f}")
            else:
                print("Divisão com zero não é permitida.")
        case 5:
            print("Saindo da calculadora.")
            break
        case _:
            print("Opção inválida. por favor escolha uma operação válida.")