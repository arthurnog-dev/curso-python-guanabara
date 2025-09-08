# Crie um algoritimo que leia um número e mostre o seu dobro, seu triplo e raiz quadrada.

numero = int(input("Digite um número: "))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5

print(f"O número selecionado foi: {numero}")
print(f"O dobro de {numero} é {dobro}.")
print(f'O triplo de {numero} é {triplo}.')
print(f'A raiz quadrada de {numero} é {raiz}.')