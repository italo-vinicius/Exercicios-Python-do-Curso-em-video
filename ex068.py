from random import randint
wins = 0
while True:
    computer = randint(0 , 10)
    print(computer)
    print('-=' * 20)
    escolha = int(input('\033[36;1mDIGITE UM NÚMERO:\033[m '))
    print('-=' * 20)
    poi = str(input('\033[35;1mPar ou Ímpar? [P/I]\033[m: ')).upper().strip()[0]
    print('-=' * 20)
    soma = computer + escolha
    if soma % 2 == 0:
        if poi == 'P':
            print(f'\033[32;1mVocê acertou. O computador jogou {computer} e a soma foi {soma}, que é um resultado par\033[m')
            wins += 1
        if poi == 'I':
            print(f'\033[31;1mVocê errou. O computador jogou {computer} e a soma foi {soma}, que é um resultado par\033[m')
            break
    if soma % 2 != 0:
        if poi == 'I':
            print(f'\033[32;1mVocê acertou. O computador jogou {computer} e a soma foi {soma}, que é um resultado impar\033[m')
            wins += 1
        if poi == 'P':
            print(f'\033[31;1mVocê errou. O computador jogou {computer} e a soma foi {soma}, que é um resultado impar\033[m')
            break
print(f'\033[35;1mFIM DE JOGO. VOCÊ ACERTOU {wins} VEZES\033[m')