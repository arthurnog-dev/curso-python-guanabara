# Escreva um programa que converta uma temperatura digitaado em ºC e converta para ºF

c = float(input('Digite a temperatura em ºC que deseja converter: '))
f = ((9*c)/5) + 32 # Também possível sem () 9*c/5+32
print(f"A temperatura de {c}ºC corresponde a {f}ºF!")