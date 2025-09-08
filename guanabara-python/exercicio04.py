# ESCREVA UM PROGRAMA QUE LEIA EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILIMETROS.

numero = float(input('Digite um valor: '))
cen = numero * 100
mili = numero * 1000

print(f'{numero}m tem {cen} centímetros e {mili} milimetros')