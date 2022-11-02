dados = []
jogador = {}
ask = 'Ss'
while ask not in 'Nn':
    jogador['NOME'] = str(input('NOME DO JOGADOR: ').upper())
    jogador['PARTIDAS'] = int(input(f'QUANTAS PARTIDAS {jogador["NOME"]} JOGOU? '))
    jogador['GOLLIST'] = []
    for c in range(1, jogador['PARTIDAS'] + 1):
        numgol = int(input(f'QUANTOS GOLS NA PARTIDA {c}? '))
        jogador['GOLLIST'].append(numgol)
    jogador['TOTGOL'] = sum(jogador['GOLLIST'])
    dados.append(jogador.copy())
    ask = str(input('QUER CONTINUAR? S/N '))
    print('-'*45)

print('=-'*30)
print(f'{"cod":<7}{"nome":<15}{"gols":<15}{"total de gols":<15}')
for c, v in enumerate(dados):
    print(f'{c:<7}{dados[c]["NOME"]}            {dados[c]["GOLLIST"]}         {dados[c]["TOTGOL"]}')
print('=-'*30)

while True:
    perg = int(input('MOSTRAR DADOS DE QUAL JOGADOR? (999 INTERROMPE) '))
    if perg < len(dados):
        print(f'LEVANTAMENTO DO JOGADOR {dados[perg]["NOME"]}:')
        totpartida = 1
        for c in dados[perg]['GOLLIST']:
            print(f'NO JOGO {totpartida} FEZ {c} GOLS')
            totpartida += 1
        print('=-'*30)
    elif perg >= len(dados) and perg != 999:
        print(f'NÃO EXISTE JOGADOR COM CÓDIGO {perg}.. TENTE NOVAMENTE!!')
    else:
        break