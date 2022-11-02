from random import randint

jkp = ['pedra', 'papel', 'tesoura']
computer = randint(0, 2)
print('[1] PEDRA\n[2] PAPEL\n[3] TESOURA')
escolha = int(input('O QUE VOCÊ ESCOLHE? '))
print('.'*100)
if computer == 0:
    print('COMPUTADOR ESCOLHEU PEDRA ')
    if escolha == 1:
        print('tbm escolhi pedra. empatamos'.upper())
    elif escolha == 2:
        print('escolhi papel. você perdeu'.upper())
    else:
        print('escolhi tesoura. você ganhou'.upper())
elif computer == 1:
    print('COMPUTADOR ESCOLHEU PAPEL ')
    if escolha == 2:
        print('tbm escolhi papel. empatamos'.upper())
    elif escolha == 3:
        print('escolhi tesoura. eu ganhei'.upper())
    else:
        print('escolhi pedra. você ganhou'.upper())
elif computer == 2:
    print('COMPUTADOR ESCOLHEU TESOURA ')
    if escolha == 3:
        print('tbm escolhi tesoura. empatamos'.upper())
    elif escolha == 2:
        print('escolhi papel. você ganhou'.upper())
    else:
        print('escolhi pedra. você perdeu'.upper())