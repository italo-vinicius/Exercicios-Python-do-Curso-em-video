p = float(input('VALOR DO PRODUTO: '))
print('FORMAS DE PAGAMENTO\n[1] á vista no dinheiro ou cheque\n[2] á vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
fp = int(input('qual forma de pagamento? '))
v = p - (p * 10/100)
vc = p - (p * 5/100)
dc = p
tc = p + (p * 20/100)
if fp == 1:
    print(f'sua compra de {p}R$ vai custar {v}R$.')
elif fp == 2:
    print(f'sua compra de {p}R$ vai custar {vc}R$.')
elif fp == 3:
    print(f'sua compra de {p}R$ vai custar {dc}R$.')
elif fp == 4:
    print(f'sua compra de {p}R$ vai custar {tc}R$.')
else:
    print('ERRO. ESCOLHA A FORMA DE PAGAMENTO NOVAMENTE!')