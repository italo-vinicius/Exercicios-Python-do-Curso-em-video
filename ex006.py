from math import sqrt as raiz
x = int(input('digite um valor: '))
d = x * 2
t = x * 3
r = raiz(x)
print(f'o dobro desse número é \033[1;31m{d}\033[m, o triplo é \033[1;34m{t}\033[m\ne sua raiz quadrada é \033[1;36m{r:.2f}\033[m')


