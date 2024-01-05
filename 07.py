"""7. Faça um Programa que pergunte em que turno você estuda. Peça para digitar:
M-matutino
V-Vespertino
N- Noturno
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

t = str(input('Digite seu turno: M-matutino, V-Vespertino, N- Noturno:  '))

if t == 'm':
    print('Bom dia!')
if t == 'v':
    print('Boa tarde!')
if t == 'n':
    print('Boa noite!')

