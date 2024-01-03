#Exemplo 2

n1 = float(input('Digite a primeira nota: '))
n2 =  float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 5:
    print('Sua média foi {}, você foi aprovado!'.format(media))
else:
    print('Sua média foi {}, você está reprovado!'.format(media))
