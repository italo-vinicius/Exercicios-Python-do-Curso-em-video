from random import randint
from time import sleep
list1 = list()
jogo = list()
quantidade = int(input('QUANTOS JOGOS VOCÊ QUER QUE EU FAÇA PARA VOCÊ? '))
totaljogo = 1
while totaljogo <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in list1:
            list1.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.append(list1[:])
    list1.clear()
    totaljogo += 1

for c in range(0, len(jogo)):
    if c == 0:
        print('GERANDO RESULTADOS...AGUARDE POR FAVOR!!')
        sleep(3)
    print(f'JOGO {c + 1}: {jogo[c]}')
    sleep(1)