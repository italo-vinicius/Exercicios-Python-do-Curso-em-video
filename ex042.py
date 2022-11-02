r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('pode se formar um triângulo')
else:
    print('não se pode formar um triângulo')
if r1 == r2 == r3:
    print('esse triângulo será: equilátero')
elif r1 == r2 or r2 == r3 or r3 == r1:
    print('esse triângulo será: isósceles')
else:
    print('esse triângulo será: escaleno')