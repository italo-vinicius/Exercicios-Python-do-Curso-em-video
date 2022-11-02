def decorar(msg):
    tam = len(msg) + 15
    print('-' * tam)
    print(f'       {msg}')
    print('-' * tam)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            if 1 <= n <= 3:
                return n
            else:
                print('\033[1;31mERRO. DIGTE UMA OPÇÃO VÁLIDA\033[m') 
        except:
            print('\033[1;31mERRO. DIGTE UMA OPÇÃO VÁLIDA\033[m')  


def fazer(op):
        if op == 1:
            arquivo = open('ex115/pessoascadastradas.txt', 'r')
            print(arquivo.read())
            arquivo.close()
        elif op == 2:
            arquivo = open('ex115/pessoascadastradas.txt', 'a')
            arquivo.write(f'\n{input("CADASTRE ALGUEM: ").upper():<11} {input("IDADE: ")} ANOS')
            arquivo.close()
