"""2. Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez."""

n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite uma nota: '))
soma = n1 + n2
media = soma / 2

if media == 10:
    print('Sua média foi {}. Você foi Aprovado com Distinção.PARABENS!'.format(media))
elif media >= 7:
    print('Sua média foi {}. Você foi Aprovado!'.format(media))
elif media <= 6:
    print('Sua média foi {}.Você foi reprovado!'.format(media))
