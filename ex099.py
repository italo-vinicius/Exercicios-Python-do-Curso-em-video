from random import randint


def maior(lst):
    print('=-='*15)
    print('ANALISANDO OS VALORES: ')
    print(f'FORAM INFORMADOS {len(lst)} VALORES AO TODO')
    print('OS VALORES FORAM: ', end='')
    for c in lst:
        print(c, end=' ')
    print()
    print(f'O MAIOR VALOR FOI {max(lst)}')


numeros = [1, 3, 5, 7, 3, 12, 16]
maior(numeros)
numeros2 = [1,56,4,3,2,1,4,65,7,8,8]
maior(numeros2)
