#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras MAIUSCULAS
#O nome com  todas as letras minusculas
#Quantas letras ao todo (sem considerar os space)
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()

print('Sue nome em letrar Maiusculas: {}'.format(nome.upper()))
print('Seu nome em letras Minusculas: {}'.format(nome.lower()))
print('Seu nome, qtas letras tem sem contar os espaços: {}'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem: {}'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))