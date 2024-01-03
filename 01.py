# numa condição somente um dos blocos sera executado

#condição
# if = bloco True
# else = Bloco False

# ex:
tempo = int(input('Quantos anos tem seu carro: '))

if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('---FIM---')

#Condição simplificada
print('carro novo' if tempo <= 3 else'carro velho')
print('---FIM---')