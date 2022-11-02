r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('digite a terceira reta:   '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('pode se formar um triângulo')
else:
    print('não se pode formar um triângulo')