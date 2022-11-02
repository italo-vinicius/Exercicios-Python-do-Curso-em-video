from random import randint
computador = randint(1, 10)
meuchute = int(input('tente acertar em que número estou pensando: '))
print(computador)
while meuchute != computador:
    meuchute = int(input('erro.tente novamente: '))
    if computador == meuchute:
        print('parabéns')
        break 