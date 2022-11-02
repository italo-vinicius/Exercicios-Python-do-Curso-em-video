n= 0 
cont = 0
soma = 0
while True:
    n = int(input('digite um número: '))
    if n != 999:
        cont += 1
        soma += n
    else:
        break
print(f'foram digitados {cont} e a soma entre eles foi {soma}')