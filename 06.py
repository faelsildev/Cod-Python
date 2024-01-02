#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#em que posição ela aprece a ultima vez

f = str(input('Digite uma frase: ')).strip()

print('A letra A aparece: '.format(f.count('a')))
print('A primeira aparição de A, ta na posição: '.format(f.find('a')))
print('A ultima aparição de A, ta na posição: '.format(f.rfind('a')))
