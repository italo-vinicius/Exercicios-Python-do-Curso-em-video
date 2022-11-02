from re import A


n = int(input('digite quantos elementos você quer ver da sequência Fibonacci: '))
antecessor = 0
somador = 1
v = 0
print(antecessor , end=' - ')
while v != n:
    somador += antecessor
    antecessor = somador - antecessor
    v += 1
    print(somador, end=' - ')
print('FIM')