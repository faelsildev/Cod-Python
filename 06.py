"""6. Faça um Programa que leia três números e mostre-os em ordem decrescente"""

primeiro = int(input('Digite um numero: '))
segundo = int(input('Digite um numero: '))
terceiro = int(input('Digite um numero: '))

if terceiro > segundo:
    aux = terceiro
    terceiro = segundo
    segundo = aux
if segundo > primeiro:
    aux = segundo
    segundo = primeiro
    primeiro = aux
if terceiro > segundo:
    aux = terceiro
    terceiro = segundo
    segundo = aux

print(primeiro,'-',segundo,'-',terceiro)

