print("-----Média escolar-----")

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))


media = (nota1 + nota2 + nota3 ) / 3

match media:
     case media if media >= 7:
        print(f"Parabéns, você foi aprovado com média de {media:.2f}!!")
     case media if media >= 5:
        print(f"Você está de recuperação, Média de {media:.2f}!!")
     case _:
        print(f"você foi reprovado, Sua média é {media:.2f}!!")
