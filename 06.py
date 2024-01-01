#o mesmo professor do desafio anterior quer sorttear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random


nome1 = str(input('Digite um nome: '))
nome2 = str(input('Digite um nome: '))
nome3 = str(input('Digite um nome: '))
nome4 = str(input('Digite um nome: '))

lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)

print('A apresentação dos alunos vai ser:')
print(lista)