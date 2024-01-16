"""Desenvolva uma logica que lleia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabella abaixo
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Morbida"""


peso = float(input('Peso: '))
altura = float(input('Altura: '))

IMC = peso / (altura ** 2)
print(IMC)

if IMC <= 18.5:
    print('Abaixo do peso.')
elif (IMC > 18.5) and (IMC <= 25):
    print('Peso Ideal')
elif (IMC > 25) and (IMC <= 30):
    print('Sobrepeso')
elif (IMC > 30) and (IMC < 40):
    print('Obesidade')
else:
    print('Obesidade Morbida')