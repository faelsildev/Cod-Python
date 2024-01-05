#1. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra  =str(input('Digite uma Vogal: '))

if letra == 'a'or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Essa letra é uma VOGAL! {}'.format(letra))
else:
    print('Essa letra é uma  CONSOANTE!')