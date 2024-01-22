"""Faça um programa que leia o peso de cionco pessoas, no final mostre qual foi o peso maior e o menor peso lidos"""

pmaior = 0
pmenor = 0

for p in range(1, 6):
    peso = float(input('O pesoda {}° pessoa: '.format(p)))

    if p == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        if peso < pmenor:
            pmenor = peso

print('O maior peso digitado foi: {}'.format(pmaior))
print('O menor peso digitado foi: {}'.format(pmenor))