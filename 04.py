#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math

an = float(input('Digite o angulo: '))

rad = math.radians(an)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print('O senho do angulo digitado é: {:.2f}'.format(seno))
print('O cosseno do angulo digitado é: {:.2f}'.format(cosseno))
print('A tangente do angulo digitado é: {:.2f}'.format(tangente))