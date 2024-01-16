"""Escreva um progama que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem
- o primeiro vallor é maior
- o segundo valor é maior
- nao existe valor maior, os 2 sao iguais"""

numero1 = int(input('Digite um valor 1: '))
numero2 = int(input('Digite um valor 2: '))

if numero1 > numero2:
    print('O numero 1 é maior.')
elif numero2 > numero1:
    print('O numero 2 é maior.')
else:
    print('Não existe valor maior.')