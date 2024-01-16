"""Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media
- media abaixo de 5.0
REPROVADO

- media entre 5.0 e 6.9
RECUPERAÇÂO

- media e7.0 ou superior
APROVADO"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
print(media)
if media < 5.0:
    print('REPROVADO')
elif media == 5 or media <= 6.9:
    print('RECUPERAÇÂO')
else:
    print('APROVADO')
