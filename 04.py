"""faça um programa que callcule a soma entre todos os numeros impares que sao multiplus de 3 e que se encontram no intervalo de 1 até 500"""
#acumulador
soma = 0
#contador
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('São {} valores acumulador e a soma de todos esses valores sao: {}'.format(cont,soma))