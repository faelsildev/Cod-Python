"""Refaça o desafio da tabuada, mostrando o numero que o usuario escollher, só que agora utilanzao o laço for"""

num = int(input('Digite um numero: '))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))