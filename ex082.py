lista = []
listapar = []
listaimpar = []
ask = 'S'
while ask not in 'N':
    lista.append(int(input(f'DIGITE UM NÚMERO: ')))
    ask = str(input('QUER CONTINUAR? [S/N]: ')).upper()
for c in range (0, len(lista)):
    if lista[c] % 2 == 0:
        listapar.append(lista[c])
    else:
        listaimpar.append(lista[c])
print(f'LISTA COMPLETA: {lista}')
print(f'LISTA DE PARES: {listapar}')
print(f'LISTA DE ÍMPARES: {listaimpar}')