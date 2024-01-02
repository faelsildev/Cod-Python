#FATIAMENTO DE STRING

frase = 'Curso em video python'

print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2]) #vai pular de 2 em 2
print(frase[:5]) #antes dos : é onde ele vai começar
print(frase[15:]) #indicou o inicio, mas nao indicou onde termina
print(frase[9::3]) #vai começar do 9 e vai até o final, os :: significa que vai pulando de 3 em 3


#ANALISE

#len = comprimento
#count = contador
#find = encontrar
#Operador in = vai retornar true ou false
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13)) #fazendo uma contagem com fatiamento
print(frase.find('deo'))
print('curso' in frase)


#TRANSFORMAÇÂO

#replace = trocar, reposicionar, substituir
#upper() = vai colorcar tudo em MAIUSCULOS
#lower() = vai colocar tudo em minusculos
#capitalize() = vai deixar somente a primeira letra em MAIUSCULO
#title() = a cada palavra depois do espaço, o title() vai colocar em MAIUSCULO
#strip() = vai remover todos os espaços desnecessario do inicio e do fim
#rstrip() = remove espaços desnecessario do lado direito
#lstrip() = remove espaços desnecessario do lado esquerdo
print(frase.replace('python', 'Python'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())


#DIVISAO
#split = vai dividir onde estiver espaços
print(frase.split())

#JUNÇÂO
#join = juntar
print('-'.join(frase))


#RELEMBRANDO
# ao utilizr 3 aspas duplas, vc consegue ler um texto grande
