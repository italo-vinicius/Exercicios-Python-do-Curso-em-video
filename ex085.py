numeros = [[], []]
n = 0
for c in range(1, 8):
    n = int(input(f'DIGITE O {c}° VALOR: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'OS VALORES PARES DIGITADOS FORAM {numeros[0]}')
print(f'OS VALORES ÍMPARES DIGITADOS FORAM {numeros[1]}')
