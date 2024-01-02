#Faça um programa que leia um numero de 0 a 9999 e mostre na tela um dos digitos separados
#ex: digite um numero: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

n = int(input('Digite um numero: '))


unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10

print('unidade: {}\n'
      'dezena: {}\n'
      'centena: {}\n'
      'milhar: {}'.format(unidade, dezena, centena, milhar))