"""Façça um programa que leia o ano de nasicmento de um jovem e informe, de acordo com sua idade
-se ele ainda vai se alistar ao serviçço militar
- se é a hora de se alistar
- se ja passou do tempo de alistamento

seu programa tambem devera mostrar o campo que falta ou que passou do prazo"""

from datetime import date

atual = date.today().year
data_nascimento = int(input('Digite a data de nascimento: '))
idade = atual - data_nascimento

print('Voçê nasceu em {} tem {} anos em {}'.format(data_nascimento, idade, atual))

if idade == 18:
    print('Está na hora de se alistar ao serviço militar.')
elif idade < 18:
    saldo = 18 - idade
    print('Falta {} para seu ano de alistamento'.format(saldo))
else:
    saldo = idade - 18
    print('Voce deveria ter se alistado há {}'.format(saldo))