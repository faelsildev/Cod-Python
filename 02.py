#Crie um programa que leia um numero qualquer pelo teclado e mostre a sua porção intetira.
#ex: 6.324,a  parte inteira é 6

import math

n = float(input('Digite um numero: '))

r = math.trunc(n)
print('O numero digitado foi {}, e a parte inteira desse numero é {}'.format(n,r))