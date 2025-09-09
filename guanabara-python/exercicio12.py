# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math

n = float(input('Digite um número: '))
ni = math.floor(n)

print(f'O número {n} tem a parte inteira {ni}.')