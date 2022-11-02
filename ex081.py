lista = []
ask = 'S'
while ask not in 'N':
    lista.append(int(input(f'DIGITE UM NÚMERO: ')))
    ask = str(input('QUER CONTINUAR? [S/N]: ')).upper()
lista.sort(reverse=True)
print(f'FORAM DIGITADOS {len(lista)} NÚMEROS')
print(f'A LISTA ORDENADA AO CONTRÁRIO: {lista}')
if 5 in lista:
    print('O VALOR 5 ESTÁ PRESENTE NA LISTA')
else:
     print('O VALOR 5 NÃO ESTÁ PRESENTE NA LISTA')

