#Desenvolva um programa que pergunte a distancia de uma viagem em km.
#Calcule o preço da passagem cobrando:
# R$0,50 por km, para viajens até 200km
# R$0,45 por km, para viagens acima de 200km

distancia = float(input('Digite a distancia a viagem: '))

print('A distancia percorrida é: {}km'.format(distancia))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.
print('O preço da sua passagem é de: R${:.2f}'.format(preco))