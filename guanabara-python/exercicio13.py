# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retãngulo, calcule e mostre o comprimento da hipotenusa.

# Com importação
#-------------------------
from math import hypot

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'O valor da hipotenusa é {hipotenusa:.2f}')

# Sem importação
#-------------------------

# cateto_oposto = float(input('Digite o valor do cateto oposto: '))
# cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

# hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5

# print(f'O valor da hipotenusa é {hipotenusa:.2f}')