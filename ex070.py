totalgasto = 0
cont = 0
maisbarato = 0
contbarato = 0
prodbarato = ' '
while True:
    produto = str(input('PRODUTO: ')).upper()
    price = float(input('PREÇO: '))
    totalgasto += price
    contbarato += 1
    if price > 1000:
        cont += 1
    if contbarato == 1:
        maisbarato = price
        prodbarato = produto
    if price < maisbarato:
        maisbarato = price
        prodbarato = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('QUER CONTINUAR? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'NA COMPRA FOI GASTO R$ {totalgasto}\n{cont} PRODUTOS CUSTAM MAIS DE R$1000\n{prodbarato} É O PRODUTO MAIS BARATO E CUSTA {maisbarato}R$')