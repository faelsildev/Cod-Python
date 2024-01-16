"""A confederação nacional de natação precisa de um programa que leia o ano de nacimento de um atleta e mostre sua categoria
de acordo com sua idade

- até 9 anos: MIRIM
- até 14 anos: INFANTTIL
- até 19 anos: JUNIOR
- até 20 anos: SENIOR
- acima: MASTER"""

from datetime import date

atual = date.today().year

data_nascimento = int(input('Data de nascimento: '))
idade = atual - data_nascimento

if idade <= 9:
    print('Categoria: MIRIM')
elif (idade > 10) and (idade <= 14):
    print('Categoria: INFANTIL')
elif (idade > 14) and (idade <= 19):
    print('Categoria: JUNIOR')
elif idade == 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')
