# Faça um algoritimo que leia osalário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Digite o seu salário R$'))
reajuste = salario + (salario*15/100)

print(f'O salário de R${salario:.2f} com o aumento vai para R${reajuste:.2f}')