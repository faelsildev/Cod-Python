#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamentte
#EX: RAFAEL APARECIDO DA SILVA
#primeiro nome: RAFAEL
#ultimo nome: SILVA

n = str(input('Digite um nome: '))
nome = n.split()

print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[-1]))