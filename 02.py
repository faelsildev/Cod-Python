"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações."""

usuario = str(input('Usuario: ')).strip()
senha = str(input('Senha: '))

while usuario == senha:
    print('O usuario nao pode ser o mesmo que a senha. mude!')
    senha = str(input('Senha: '))

print('Cadastro aprovado')
