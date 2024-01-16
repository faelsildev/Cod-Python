"""Escreva um progama para aprovar um emprestimo bancario para compra de uma casa.O progama vai perguntar o valor da casa,
o salario do comprador e em quantos anos ele vai pagar.

calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salalrio ou entao o emprestimo sera negado"""

valor_casa = float(input('Digite o valor da casa: R$ '))
salario_comprador = float(input('Digite o salario do comprador: R$ '))
anos_pagar = int(input('Quantos anos deseja pagar? '))

prestacao = valor_casa / (anos_pagar * 12)
minimo = (salario_comprador * 30) / 100

print('Para pagar uma casa de R${} em {} anos,'.format(valor_casa, anos_pagar), end='')
print(' A prestação vai ser de R${}'.format(prestacao))

if prestacao <= minimo:
    print('Esmprestimo concedido')
else:
    print('Emprestimo negado.')


#OBS: Achei MEDIANO