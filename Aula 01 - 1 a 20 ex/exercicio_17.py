print("--------analise de numeros--------")
 
numeros = []

for i in range(10):
    numero = int(input(f"digite o {i+1} número: "))
    numeros.append(numero)
print()

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A média dos números é: {media:.2f}")
