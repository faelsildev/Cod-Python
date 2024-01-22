"""Crie um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50"""

for c in range(1,51):
    if c % 2 == 0:
        print('O numero {}, é par.'.format(c))
    else:
        print('O numero {}, não é par.'.format(c))



#Outra forma

for c in range(2, 51, 2):
    print(c, end=' ')
print('Acabaou')