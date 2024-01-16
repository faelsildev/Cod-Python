"""Escreva um programa que leia um neumero inteiro qualquer e pea para o usuario escolher qual sera a base de conversao
- 1 para BINARIO
- 2 para OCTAL
- 3 para HEXADECIMAL"""

num = int(input('Digite um numero inteiro: '))
print("""Escola uma das base para conversão:

- 1 para BINARIO
- 2 para OCTAL
- 3 para HEXADECIMAL

""")

escolher = int(input('Escolha entre: [1], [2] ou [3]: '))

if escolher == 1:
    print('O numero {} convertido para BINARIO é: {}'.format(num, bin(num)))
elif escolher == 2:
    print('O numero {} convertido para OCTAL é: {}'.format(num, oct(num)))
else:
    print('O numero {} convertido para HEXADECIMAL é: {}'.format(num, hex(num)))