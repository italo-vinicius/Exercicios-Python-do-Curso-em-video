from random import choice

a1 = str(input('\033[1;36;40maluno 1:\033[m '))
a2 = str(input('\033[1;37;40maluno 2:\033[m '))
a3 = str(input('\033[1;33;40maluno 3:\033[m '))
a4 = str(input('\033[1;35;40maluno 4:\033[m '))
lista = [a1, a2, a3, a4 ,]
print(f'O ALUNO SORTEADO FOI: \033[7;31;40m{choice(lista)}\033[m')
