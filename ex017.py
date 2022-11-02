import math

c1 = float(input('\033[1;34;40m digite o cateto 1:\033[m '))
c2 = float(input('\033[1;32;40m digite o cateto 2:\033[m '))
h = math.pow(c1, 2) + math.pow(c2, 2)
x = math.sqrt(h)
print(f'a \033[4;36m hipotenusa\033[m é igual á \033[1;107;40m{x:.2f}\033[m')
