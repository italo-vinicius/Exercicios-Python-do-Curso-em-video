def leiaInt(msg):
    """
    exemplo docstring
    """
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('ERRO..DIGITE UM NÚMERO INTEIRO')  

n = leiaInt('DIGITE APENAS NÚMERO: ')
print(f'VOCÊ ACABOU DE DIGITAR O VALOR {n}')


