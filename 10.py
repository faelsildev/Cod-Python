"""Crie um programa que leia o ano de nascimento de sete pessoas. no final mostre quantas pessoas ainda nao atingiram a maioridade e quantats ja sao maiores"""

from datetime import date
totmaior = 0
totmenor = 0

atual =  date.today().year
for c in range(1,8):
    nasc  = int(input('Digite a {}° data de nascimento: '.format(c)))
    idade =   atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas  maiores de idade.'.format(totmaior))
print('Ao todo tivemos {} pessoa menores  de idade.'.format(totmenor))