#faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o numero: '))
n2 = int(input('Digite o numero: '))
n3 = int(input('Digite o numero: '))
menor = n1
#verificando quem é menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#testando quem é maior
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor numero digitado foi {}'.format(menor))
print('O maior numero digitado foi {}'.format(maior))



