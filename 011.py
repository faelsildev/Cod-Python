"""Cie um programa que faça o computador jogar jokenpo com vc"""
from random import randint

print("""DIGITE
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA""")

digite = str(input('DIGITE: '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('O computador escolheu: {}'.format(itens[computador]))
print('O jogador jogou')
if digite == 1:
