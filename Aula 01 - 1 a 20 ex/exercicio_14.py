print("------- Função calculadora-------")

def soma(num1, num2):
    return num1 + num2

num1 = float(input("Digite o primeiro número: "))
print()
num2 = float(input("Digite o segundo número: "))
print()


resultado = soma(num1, num2)
print(f"O resultado da soma é: {resultado:.2f}")