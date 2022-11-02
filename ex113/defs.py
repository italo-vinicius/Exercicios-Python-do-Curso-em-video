def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except (KeyboardInterrupt):
            print('\033[1;34mO USUÁRIO NÃO QUIS INFORMAR O VALOR\033[m')
            return '**'
        except:
            print('\033[1;31mERRO..DIGITE UM NÚMERO INTEIRO\033[m')  

        

def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
            return f
        except (KeyboardInterrupt):
            print('\033[1;34mO USUÁRIO NÃO QUIS INFORMAR O VALOR\033[m')
            return '**'
        except:
            print('\033[1;31mERRO..DIGITE UM NÚMERO REAL\033[m')