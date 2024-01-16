"""Refaça o desafio dos triangulos, acrecentando o recurso de mostrar tipo de triangulo sera formado:
- EQUILLATERO: todos os lados iguais
- ISÓCELES: dois lados iguais
- ESCALENO: todos os lados diferente"""

lado1 = float(input('Digite o primeiro lado do triangulo: '))
lado2 = float(input('Digite o segundo lado do triangulo: '))
lado3 = float(input('Digite o terceiro lado do triangulo: '))

if lado1 == lado2 == lado3:
    print('Esse triangulo é EQUILATERO!')
elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado1 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2 or lado3 == lado2 != lado1:
    print('Esse triangulo é ISÓCELES!')
else:
    print('Esse triangulo é ESCALENO!')