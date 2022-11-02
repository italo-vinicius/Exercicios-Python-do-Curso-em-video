listainput = list()
dadosfull = list()
ask = 'Ss'
while ask not in 'Nn':
    listainput.append(str(input('NOME: ')))
    listainput.append(float(input('NOTA 1: ')))
    listainput.append(float(input('NOTA 2: ')))
    ask = str(input('QUER CONTINUAR? [S/N] '))
    dadosfull.append(listainput[:])
    listainput.clear()
    
print('=-'*15)
print('No.     ALUNO         MÉDIA')
print('-'*30)

for pos, alun in enumerate(dadosfull):
    print(f'{pos} {alun[0]:>10} {(alun[1]+alun[2])/2:>15.2f}')

pos = 0
while pos != 999:
    pos = int(input('MOSTRAR NOTAS DE QUAL ALUNO? (999 INTERROMPE) '))
    print(f'AS NOTAS DE {dadosfull[pos][0]} FORAM {dadosfull[pos][1]} e {dadosfull[pos][2]}')
    