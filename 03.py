"""3. Faça um Programa que leia três números inteiros e mostre o maior deles."""

n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite um numero inteiro: '))
n3 = int(input('Digite um numero inteiro: '))

maior = n1

if n1 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('Maior: {}'.format(maior))