# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = int(input('Digite quanto dinheiro você tem: '))
dolar = 5.20

resultado = reais / dolar

print(f'Você pode comprar {resultado:.2f} dólares')