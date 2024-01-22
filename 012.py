"""desenvolva um programa que leia o nome, idade e sexo de 4 pessos, no final do programa mostre:

- A media de idade do grupo
- Qual é o nome da pessoa mais velha
- Quantas pessoas tem menos de 20 anos"""

from datetime import date

atual =  date.today().year

print("""ESCOLHA AS SEGUINTES SIGLAS:
        [F] - Feminino
        [M] - Masculino
        [O] - Outros\n""")

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for c in range( 1, 5):
    print('---------{}° PESSOA-------'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somaidade += idade
    if c ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade /4

print('A media de idade do grupo é {}'.format(mediaidade))
print('A pessoa mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))












