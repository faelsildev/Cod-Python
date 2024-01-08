"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;"""

lado1 = float(input('Digite um lado do Triangulo: '))
lado2 = float(input('Digite um lado do Triangulo: '))
lado3 = float(input('Digite um lado do Triangulo: '))

if lado1 == lado2 == lado3:
    print('Esse é um triangulo EQUILATERO!')
elif lado1 == lado2 != lado3:
    print('Esse é i, triangulo ISÓCELES!')
elif lado1 != lado2 != lado3:
    print('Esse  é um triangulo ESCALENO')
