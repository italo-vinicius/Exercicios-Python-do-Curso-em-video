from random import randint

def sorteio(lst):
    print('OS VALORES SORTEADOS FORAM: ', end='')
    for c in range(1, 6):
        numeros.append(randint(1, 20))
    print(numeros, end=' ')
    print()

def somaPar(lst):
    print('A SOMA DOS VALORES PARES É: ', end='')
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(soma)


numeros = []
sorteio(numeros)
somaPar(numeros)