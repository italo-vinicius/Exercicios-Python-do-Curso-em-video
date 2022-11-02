fatorial = int(input('digite um número para caucular o fatorial: '))
c = fatorial
f = 1
while fatorial != 0:
    f *= fatorial
    fatorial -= 1
print(f'o fatorial de {c} é: {f}', end=' ')
    