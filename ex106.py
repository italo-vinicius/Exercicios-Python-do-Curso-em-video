c = (
    '\033[m',
    '\033[1;30;41m',
    '\033[1;30;44m',
    '\033[30;45m',
    '\033[1;30;42m'
)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam) 
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


def ajuda(comando):
    titulo(f'ACESSANDO ARQUIVOS DO COMANDO \'{comando}\'', 2)
    print(c[4], end='')
    help(comando)
    print(c[0], end='')


comando = ' '
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('FUNÇÃO OU BIBLIOTECA > ')).lower()
    if comando == 'fim':
        titulo('FIM', 3)
        break
    else:
        ajuda(comando)