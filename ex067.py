while True:
    t = int(input('QUER VER A TABUADA DE QUAL NÚMERO? '))
    if t < 0:
        break
    for c in range(0, 11):
        print(f'{t} X {c} = {t * c}')
