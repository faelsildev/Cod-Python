"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres)."""

no = str(input('Nome: ')).strip()
idade = int(input('Idade: '))
salario = float(input('Salario: '))
sexo = str(input('Sexo: [F/M]: ')).upper()
etc = str(input('Estado civil: [S- Solteiro(a)], [C- Casado(a)], [V- Viuvo(a)], [D- Divorciado(a)]: ')).upper()

while len(no) <= 3:
    no = str(input('Nome precisa ter mais do que 3 caracter. Digite novamente: '))
while (idade < 0) or (idade > 150):
    idade = int(input('Idade precisa ter entre 0 e 150. Digite novamente: '))
while salario < 0:
    salario = float(input('Digite um salario valido: '))
while sexo != 'f' and sexo != 'm':
    sexo = str(input('Digite [F] - Feminino ou [M] - Masculino: '))
while etc != 's' and etc != 'c' and etc != 'v' and etc != 'd':
    etc = str(input('Estado civil: [S],[C],[V],[D]'))

print('Todos os dados inseridos corretamente!')

