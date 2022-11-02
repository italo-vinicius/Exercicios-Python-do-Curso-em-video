valor = int(input('\033[1;34mQUAL VALOR VOCÊ VAI SACAR?\033[m '))
n50 = n20 = n10 = n1 = 0
novovalor = 0
while True:
    n50 = valor // 50
    novovalor = valor - n50 * 50
    if novovalor != 0:
        n20 = novovalor // 20
        novovalor -= n20 * 20
    if novovalor != 0:
        n10 = novovalor // 10
        novovalor -= n10 * 10
    if novovalor != 0:
        n1 = novovalor // 1
        novovalor -= n1 * 1
    break
print('\033[7;97;40mVOCÊ VAI RECEBER...\033[m')
if n50 != 0:
    print(f'\033[1;32m{n50} CÉDULAS DE R$50\033[m')
if n20 != 0:
    print(f'\033[1;32m{n20} CÉDULAS DE R$20\033[m')
if n10 != 0:
    print(f'\033[1;32m{n10} CÉDULAS DE R$10\033[m')
if n1 != 0:
    print(f'\033[1;32m{n1} CÉDULAS DE R$1\033[m')
    