#Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome "SANTO"

c = str(input('Digite o nome da cidade: ')).strip()

print(c[:5].upper() == 'SANTO')

