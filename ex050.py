s = 0
for c in range(1, 7):
    n = (int(input('diga um número: ')))
    if n % 2 == 0:
        s += n
    else:
        continue
print(f'a soma dos pares será {s}')
