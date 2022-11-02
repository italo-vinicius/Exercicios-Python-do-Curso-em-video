n1 = int(input('\033[1;32mDIGITE UM NÚMERO:\033[m '))
n2 = int(input('\033[1;32mDIGITE OUTRO NÚMERO:\033[m '))
n3 = int(input('\033[1;32mDIGITE OUTRO NÚMERO:\033[m '))
n4 = int(input('\033[1;32mDIGITE MAIS UM NÚMERO\033[m '))
numeros = (n1, n2, n3, n4)
print('-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'\033[1;35mVOCÊ DIGITOU OS VALORES {numeros}\033[m')
print(f'O NÚMERO 9 APARECEU {numeros.count(9)} VEZES')
if 3 in numeros:
    print(f'O NÚMERO 3 APARECEU PELA PRIMEIRA VEZ NA POSIÇÃO {numeros.index(3) + 1}')
else:
    print('O NÚMERO 3 NÃO APARECEU NA LISTA')
print('OS NÚMEROS PARES FORAM: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=" ")








# contpar = 0
# if n1 % 2 == 0:
#     contpar +=1
# if n2 % 2 == 0:
#     contpar +=1
# if n3 % 2 == 0:
#     contpar +=1
# if n4 % 2 == 0:
#     contpar +=1
# print(f'APARECERAM {contpar} NÚMEROS PARES')

