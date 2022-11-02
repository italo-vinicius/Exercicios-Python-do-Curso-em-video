from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('OS NÚMEROS SORTEADOS FORAM: ', end='')
for c in range (0, 5):
    print(numeros[c], end=' ')
print(f'\nO MAIOR NÚMERO FOI {max(numeros)} E O MENOR FOI {min(numeros)}')