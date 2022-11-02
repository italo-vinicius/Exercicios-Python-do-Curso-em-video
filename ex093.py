ficha = {
    'NOME' : str(input('NOME DO JOGADOR: ').upper()),
}
gol = []
partidas = int(input(f'QUANTAS PARTIDAS {ficha["NOME"]} JOGOU? '))
totalgol = 0
for c in range(1, partidas + 1):
    numgol = int(input(f'QUANTOS GOLS NA PARTIDA {c}? '))
    gol.append(numgol)
    totalgol += numgol
ficha['GOLS'] = gol
ficha['TOTAL DE GOLS'] = totalgol
print('=-'*30)
print(ficha)
print('=-'*30)
for c, v in ficha.items():
    print(f'O CAMPO {c} TEM O VALOR {v}')
print('=-'*30)
print(f'O JOGADOR {ficha["NOME"]} JOGOU {partidas} PARTIDAS')
for c in range(1, partidas + 1):
    print(f'=> NA PARTIDA {c} FEZ {ficha["GOLS"][c - 1]} GOLS')
print(f'FOI UM TOTAL DE {totalgol} GOLS')