print("-------Classificação por idade-------")

idade = int(input("Digite a sua idade: "))


match idade:
    case idade if idade <= 0:
        print("Por favor digite uma idade maior que 0.")

    case idade if idade <= 12:
        print("Você é uma criança")

    case idade if idade <= 17:
        print("Você é um adolescente")

    case idade if idade <= 67:
        print("Você é um adulto")
        
    case _:
        print("Você é um idoso")