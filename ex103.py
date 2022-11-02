def ficha(jog='<<DESCONHECIDO>>',  gol=0):
    print(f'O JOGADOR {jog} FEZ {gol} GOLS NO CAMPEONATO ')


nome = str(input('NOME DO JOGADOR: '))
gols = str(input('TOTAL DE GOLS MARCADOS: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)