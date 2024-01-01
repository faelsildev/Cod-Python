#um professor quer sortear um dos seus quatro alunos para apagar o quadro, faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
import random

nome1 = input('Digite um nome: ')
nome2 = input('Digite um nome: ')
nome3 = input('Digite um nome: ')
nome4 = input('Digite um nome: ')

lista = [nome1, nome2, nome3, nome4]

sorteio = random.choice(lista)

print('O nome sorteado é: {}'.format(sorteio))