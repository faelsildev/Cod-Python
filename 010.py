#escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a R$ 1.250,00, calule um aumento de 10%
#Para salarios inferiores a R$ 1.250,00, calcule um aumento de 15%

salario = float(input('Digite o salario: '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O seu salario era R${}, com o aumento foi para {}'.format(salario, novo))