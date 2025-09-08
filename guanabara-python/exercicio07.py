# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. sabendo que cada litro de tinta pinta uma área de 2m².

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura

tinta = area / 2

print(f'A quantidade de tinta necessária para pintar sua parede é de {tinta:.2f} litros')