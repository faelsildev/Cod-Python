# escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite

print('Velocidade minima da via 80Km/h \n')

c = int(input('Qual a velocidade do carro? '))
macl = 7

if c <= 80 :
    print('Você está dentro do limite de velocidade estabelecido pela rodovia!')
else:
    print('Voce  esta a cima do limire de velocidade estabellecido pela via. MULTADO')
    c = (c - 80) * 7
    print('A multa vai ficar no valor de: R${}'.format(c))