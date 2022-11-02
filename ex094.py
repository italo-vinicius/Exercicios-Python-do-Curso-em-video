dados = []
cadastro = {}
ask = 'Ss'
totalidade = 0
while ask not in 'Nn':
    cadastro['NOME'] = str(input('NOME: ').upper())
    while True:
        cadastro['SEXO'] = str(input('SEXO: M/F ').upper()[0])
        if cadastro['SEXO'] in 'MF':
            break
        print('ERRO..TENTE NOVAMENTE [M/F] ')
    cadastro['IDADE'] = int(input('IDADE: '))
    totalidade += cadastro['IDADE']
    dados.append(cadastro.copy())
    ask = str(input('QUER CONTINUAR? S/N '))
print('=-'*30)
media = totalidade / len(dados)
print(f'-   O GRUPO TEM {len(dados)} PESSOAS')
print(f'-   A MÉDIA DE IDADE É {media:.2f} ANOS')

print(f'-   AS MULHERES CADASTRADAS FORAM: ', end='')
for p in dados:
    if p['SEXO'] in 'Ff':
        print(f'{p["NOME"]}', end=' ')

    
for pos in range(0, len(dados)):
    if pos == 0:
            print('\n-  PESSOAS ACIMA DA MÉDIA:')
    if dados[pos]['IDADE'] > media:
        print(f'\nNOME = {dados[pos]["NOME"]}; SEXO = {dados[pos]["SEXO"]}; IDADE = {dados[pos]["IDADE"]}')
        if pos == len(dados):
            print('<<ENCERRADO>>')

