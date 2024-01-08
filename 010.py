"""10. .Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0                      A
      Entre 7.5 e 9.0                        B
      Entre 6.0 e 7.5                        C
      Entre 4.0 e 6.0                        D
      Entre 4.0 e zero                      E
    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."""

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

if media >= 9:
    conceito = 'A'
elif media >= 7.5:
    conceito = 'B'
elif media >= 6:
    conceito = 'C'
elif media >=4:
    conceito = 'D'
elif media >= 0:
    conceito = 'E'

if conceito == 'A' or 'B' or 'C':
    situacao = 'APROVADO!'
elif conceito == 'D' or 'E':
    situacao = 'REPROVADO!'

print('*'*10)
print('Nota1: {}\n'
      'Nota2: {}'.format(nota1, nota2))
print('*'*10)
print('\n')
print('Média: {}'.format(media))
print('Conceito: {}'.format(conceito))
print('Situação: {}'.format(situacao))


