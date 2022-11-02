cadastro = list()
dados = list()
ask = 'Ss'
maior = menor = 0
while ask not in 'Nn':
    cadastro.append(str(input('NOME: ')))
    cadastro.append(float(input('PESO: ')))
    if len(dados) == 0:
        maior = menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]
    dados.append(cadastro[:])
    cadastro.clear()
    ask = str(input('QUER CONTINUAR? S/N : '))

print(f'AO TOTAL FORAM CADASTRADAS {len(dados)} PESSOAS')
print(f'O MAIOR PESO REGISTRADO FOI DE {maior}KG DAS SEGUINTES PESSOAS: '.upper(), end='')
for c in dados:
    if c[1] == maior:
        print(f'[{c[0]}]', end=' ')
print(f'\nO MENOR PESO REGISTRADO FOI DE {menor}KG DAS SEGUINTES PESSOAS: '.upper(), end='')
for j in dados:
    if j[1] == menor:
        print(f'[{j[0]}]', end=' ')