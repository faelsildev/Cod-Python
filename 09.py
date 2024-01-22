"""Crie um programa que leia uma frase qualquer e diga se ela é uma polindromo, desconsiderando os espaços

polindromo: é quqlquer frase que lendo de tras para frente é a mesma coisa

ex:apos a sopa
"""

frase =  str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('é um Palindromo!')
else:
    print('Não é um palindromo!')