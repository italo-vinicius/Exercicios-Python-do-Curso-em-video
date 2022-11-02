from time import sleep
def cont(i, f, p):
    print('=-'*30)
    if p < 0:
        p *= -1
    print(f'CONTAGEM DE {i} ATÉ {f} PULANDO DE {p} EM {p}')
    if i > f:
        p *= -1
    for c in range(i, f + 1, p):
        print(c, end=' ', flush=True)
        sleep(0.3)
    print('FIM!')


cont(1, 10, 1)
cont(10, 0 , -2)
print('-=' * 15)
print('AGORA É SUA VEZ')
ini = int(input('INÍCIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
cont(ini, fim, passo)