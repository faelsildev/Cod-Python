"""Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""

nota = int(input('Nota: '))

while (nota < 0) or (nota > 10):
    nota = float(input('nao pode ser menor que 0 ou maior que 10! '))
print('nota ok')