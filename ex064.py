leitor = int(input('digite um número inteiro: '))
cont = 0
soma = 0
while leitor != 999:
    cont += 1
    soma += leitor
    leitor = int(input('digite um número inteiro: '))
print(f'foram digitados {cont} números e a soma entre eles é de {soma}')