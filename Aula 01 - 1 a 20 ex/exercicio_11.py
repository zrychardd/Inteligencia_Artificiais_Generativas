print("-------Tabuada-------")
print()

numero =int(input("Digite o numero para saber a Tabuada : "))

print()
print (f"Tabuada de {numero}:")
print()

for i in range (1,11):
    resultado = numero * i
    print (f"{numero} X {i} = {resultado}")
print()