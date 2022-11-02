from functions import decorar, leiaInt, fazer

decorar('MENU PRINCIPAL')

print('1 - VER PESSOAS CADASTRADAS')
print('2 - CADASTRAR NOVAS PESSOAS')
print('3 - FECHAR PROGRAMA')

print('-'*29)

while True:
    escolha = leiaInt('SUA OPÇÃO: ')
    if escolha == 3:
        break
    else:
        fazer(escolha)