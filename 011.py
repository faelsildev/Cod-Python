#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo

r1 = float(input('Digite uma reta: '))
r2 = float(input('Digite uma reta: '))
r3 = float(input('Digite uma reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triangulo:')
else:
    print('Os segmentos nao podem formar um triangulo!')