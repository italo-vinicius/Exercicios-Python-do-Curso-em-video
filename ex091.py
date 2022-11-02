from operator import itemgetter
from random import randint
from time import sleep

print('OS VALORES SORTEADOS FORAM: ')
dados = {}
ranking = {}
dados['JOGADOR 1'] = randint(1, 6)
dados['JOGADOR 2'] = randint(1, 6)
dados['JOGADOR 3'] = randint(1, 6)
dados['JOGADOR 4'] = randint(1, 6)
for c, v in dados.items():
    print(f'O {c} TIROU {v}')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print(f'{"===RANKING===":>30}')
c = 1
for k, v in ranking:
    print(f'{c:>12}°:   {k} TIROU {v}')
    c += 1