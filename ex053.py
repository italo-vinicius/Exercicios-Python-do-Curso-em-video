frase = str(input('DIGITE UMA FRASE: ')).replace(' ', '')
print('*' * 50)
print(f'\033[1;34mO INVERSO DA FRASE É:\033[m')
for c in frase[::-1]:
    print(c, end='')
print(' ')
print(f'\033[1;34mA FRASE NORMAL FICA ASSIM:\033[m\n{frase}')
print('*' * 50)
if frase == frase[::-1]:
    print('A FRASE É UM PALINDROME')
else:
    print('A FRASE NÃO É UM PALINDROME')
