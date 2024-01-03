#Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o  numero escolhido pelo computador
#O programa deverá escrever  na tela se o numero do usuario venceu ou perdeu
import random
from time import sleep

escolher = int(input('Digite o numero que você escolheu: '))
print('PROCESSANDO...')
sleep(4)
n = random.randint(0,5)

if escolher == n:
    print('Voce venceu o jogo!')
else:
    print('Voce perdeu o jogo!, tente novamente.')



