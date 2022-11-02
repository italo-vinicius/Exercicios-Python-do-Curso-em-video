pt = int(input('primeiro termo da PA: '))
r = int(input('razão: '))
somador = pt
contador = 0
while contador < 9:
    if contador == 0:
        print('os 10 primeiros termos são:')
    if contador == 0:
        print(pt, end="-")
    contador += 1
    somador += r
    print(somador, end="-")