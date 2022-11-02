def dobro(n, form=False):
    if form == False:
        return n * 2
    else:
        return f'R${n * 2:.2f}'

def metade(n, form=False):
    if form == False:
        return n / 2
    else:
        return f'R${n / 2:.2f}'

def aumentar(n, porc=0, form=False):
    if form == False:
        return n + (n * (porc/100))
    else:
        return f'R${n + (n * (porc/100)):.2f}'

def diminuir(n, porc=0, form=False):
    if form == False:
        return n - (n * (porc/100))
    else:
        return f'R${n - (n * (porc/100)):.2f}'

def moeda(v):
    return f'R${v:.2f}'

def resumo(n, porc=0, porc2=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'PREÇO ANALISADO: {"R$":>7}{n}'.replace('.',','))
    print(f'DOBRO DO PREÇO: {dobro(n, True):>12}'.replace('.',','))
    print(f'METADE DO PREÇO: {metade(n, True):>12}'.replace('.',','))
    print(f'AUMENTO DE {porc}%: {aumentar(n, porc, True):>12}'.replace('.',','))
    print(f'REDUÇÃO DE {porc2}%: {diminuir(n, porc2, True):>12}'.replace('.',','))
    print('-'*30)