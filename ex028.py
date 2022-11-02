from random import randint
from time import sleep

computer = randint(0, 5)
print('\033[1;31m*\033[m' * 200)
f = 'vou pensar em um número entre 0 e 5. Tente acertar...'
print(f.upper())
print('\033[1;31m*\033[m' * 200)
jogador = int(input('\033[35mQUAL NÚMERO ESTOU PENSANDO?\033[m '))
sleep(3)
if jogador == computer:
    print('\033[1;32mACERTOU MIZERAVI\033[M')
else:
    print(f'\033[1;32mKKKKKSKS ERROU FDP..PENSEI EM {computer}')