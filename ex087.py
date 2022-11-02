matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'DIGITE UM VALOR PARA POSIÇÃO ({l},{c}): '))
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('')
print('=-'*30)
somapares = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
print(f'A SOMA DOS PARES É {somapares}')
soma3coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        if c == 2:
            soma3coluna += matriz[l][c]
print(f'A SOMA DOS VALORES DA TERCEIRA COLUNA É {soma3coluna}')
maior = list()
for l in range(0, 3):
    for c in range(0, 3):
        if l == 1:
            maior.append(matriz[l][c])
print(f'O MAIOR VALOR DA SEGUNDA LINHA É {max(maior)}')
