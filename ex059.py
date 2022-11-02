n1 = float(input('digite o primeiro valor: '))
n2 = float(input('digite o segundo valor: '))
escolha = int(input('[1]SOMAR \n[2]MULTIPLICAR \n[3]MAIOR \n[4]NOVOS NÚMEROS \n[5]SAIR DO PROGRAMA '))
while True:
    if escolha == 1:
        print(n1 + n2)
        break
    if escolha == 2:
        print(n1 * n2)
        break
    if escolha == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
            break
        else:
            print(f'{n2} é maior que {n1}')
            break
    if escolha == 4:
        novonum = float(input('digite novos valores: '))
        print(f'{n1}, {n2}, {novonum}')
        break
    if escolha == 5:
        break 
    