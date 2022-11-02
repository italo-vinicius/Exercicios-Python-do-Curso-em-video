# nummatrix = 0
# matrix = [[], [], [], [], [], [], [], [], []]
# for c in range(0, 9):
#     nummatrix = int(input('DIGITE UM VALOR: '))
#     matrix[c].append(nummatrix)
# print(f'{matrix[0]}{matrix[1]}{matrix[2]}\n{matrix[3]}{matrix[4]}{matrix[5]}\n{matrix[6]}{matrix[7]}{matrix[8]}')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'DIGITE UM VALOR PARA POSIÇÃO ({l},{c}): '))
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('')