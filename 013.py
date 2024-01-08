"""Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
 As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
  O programa não deve se preocupar com a quantidade de notas existentes na máquina."""

saque = int(input('Valor do saque: '))


if saque < 10 or saque > 600:
    print('Saque  não disponivel.')
else:
    cem = saque // 100
    saque -= cem * 100

    cinquenta = saque // 50
    saque -= cinquenta * 50

    dez = saque // 10
    saque -= dez * 10

    cinco = saque // 10
    saque -= saque * 5

    um = saque // 1
    saque -= um * 1

    if cem > 0:
        print('{} notas de cem'.format(cem))
    if cinquenta > 0:
        print('{} notas de cinquenta'.format(cinquenta))
    if dez > 0:
        print('{} notas de dez'.format(dez))
    if cinco > 0:
        print('{} notas de cinco'.format(cinco))
    if um > 0:
        print('{} notas de cem'.format(um))

#OBS: TENHO DUVIDAS  SOBRE O COD
