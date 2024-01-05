"""4. Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles."""
from time import sleep

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

print('VERIFICANDO... \n')
sleep(4)

maior = n1
if n1 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print('*'*20)
print('O maior numero é {}.'.format(maior))

menor =  n1
if n1 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print('*'*20)
print('O menor numero é {}'.format(menor))