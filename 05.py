#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

n = str(input('Digite seu nome: ')).strip()
print('SILVA' in n.upper())