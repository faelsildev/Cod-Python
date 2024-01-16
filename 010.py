"""Elabore um programa que calculle o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
- a vista DINHEIRO/CHEQUE: 10% de desconto
- a vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou amis no cartão: 20% de juros"""

preco = float(input('Preço do produto: '))

print(""" ESCOLHA UMA FORMA DE PAGAMENTO!
[1]- A vista DINHEIRO/CHEQUE: 10% de desconto
[2]- a vista no cartão: 5% de desconto
[3]- em até 2x no cartão: preço normal
[4]- 3x ou mais no cartão: 20% de juros""")

escolha = int(input('Digite a forma de pagamento: '))

if escolha == 1:
    vista = preco - (preco * 10 / 100)
    print('O preço do produto é R$ {}, com o desconto de 10%,'.format(preco),end='')
    print('vai ser R${}'.format(vista))
elif escolha == 2:
    vista_cartao = preco - (preco * 5 / 100)
    print('O preço do produto é R$ {}, com o desconto de 5%,'.format(preco), end='')
    print('vai sser R$ {}'.format(vista_cartao))
elif escolha == 3:
    parecelado2 = preco / 2
    print('O preço do produto é R$ {}, parcelado em 2x,'.format(preco), end='')
    print('fica 2x de R$ {}'.format(parecelado2))
elif escolha == 4:
    qtd_parc = int(input('Quantas parcelas? '))
if qtd_parc >= 3:
    preco_novo = preco + (preco * 20 / 100)
    parcelado3 = preco_novo / qtd_parc
    print('O preço do produto é R$ {},parcelado em {}x,'.format(preco, qtd_parc), end='')
    print('com o aumento de 20%, fica R$ {}.'.format(preco_novo), end='')
    print('A quantidade de parcelas saira R$ {}'.format(parcelado3))



