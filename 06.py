"""Desenvolva um programa que leia seis numeros inteiros e mostttre a soma apenas daqueles que forem pares, se o valor digitado for impar, desconsidere-os"""
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informar {} numeros Pares, e a soma foi {} '.format(cont, soma))