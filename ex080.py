lista = []
z = 'S'
while not z == 'N':
    x = int(input('Digite um valor: '))
    for c in range(0, len(lista)+1):
        if len(lista) == 0:
            lista.insert(0, x)
            print(f'{x} foi adicionado na posição {c}...')
            break
        elif x < lista[c]:
            lista.insert(c, x)
            print(f'{x} foi adicionado na posição {c}...')
            break
        elif x > max(lista):
            lista.append(x)
            print(f'{x} foi adicionado no final da lista...')
            break
        else:
            t = 1
    z = input('quer continuar [S/N] ?').upper()
print(f'Os nurmeos organizados são: {lista}')
