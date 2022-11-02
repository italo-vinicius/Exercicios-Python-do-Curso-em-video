#for c in range(1, 10):
#    print(f'\033[1;31mTABUADA DO {c}\033[m')
 #   for j in range(1, 10):
  #      print(f'{c} * {j} = {c*j} ')

n = int(input('digite um número para fazer a tabuada: '))
for c in range(0, 11):
    print(f'{n} * {c} = {c*n}')