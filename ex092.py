from datetime import date
dados = {'NOME': [],
        'ANO DE NASCIMENTO': [],
        'CARTEIRA DE TRABALHO':  [],
        'ANO DE CONTRATAÇÃO' : [],
        'SALÁRIO' : []
}
while True:
    dados['NOME'] = str(input('NOME: '))
    dados['ANO DE NASCIMENTO'] = int(input('ANO DE NASCIMENTO: '))
    dados['CARTEIRA DE TRABALHO'] = int(input('CARTEIRA DE TRABALHO: '))
    if dados['CARTEIRA DE TRABALHO'] == 0:
        break
    dados['ANO DE CONTRATAÇÃO'] = int(input('ANO DE CONTRATAÇÃO: '))
    dados['SALÁRIO'] = float(input('SALÁRIO: '))
    break

idade = date.today().year - dados['ANO DE NASCIMENTO']
aposentadoria = 35 - (date.today().year - dados['ANO DE CONTRATAÇÃO']) 
print('=-'*30)
if dados['CARTEIRA DE TRABALHO'] == 0:
    print(f'NOME TEM O VALOR {dados["NOME"]}')
    print(f'IDADE TEM O VALOR {idade}')
    print(f'CTPS TEM O VALOR 0')
else:
    print(f'NOME TEM O VALOR {dados["NOME"]}')
    print(f'IDADE TEM O VALOR {idade}')
    print(f'CTPS TEM O VALOR {dados["CARTEIRA DE TRABALHO"]}')
    print(f'CONTRATAÇÃO TEM O VALOR {dados["ANO DE CONTRATAÇÃO"]}')
    print(f'SALÁRIO TEM O VALOR {dados["SALÁRIO"]}R$')
    print(f'VAI SE APOSENTAR COM {idade + aposentadoria} ANOS')