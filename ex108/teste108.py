import funções108

p = float(input('DIGITE O PREÇO: R$'))
print(f'A METADE DE {funções108.moeda(p)} É {funções108.moeda(funções108.metade(p))}')
print(f'O DOBRO DE {funções108.moeda(p)} É {funções108.moeda(funções108.dobro(p))}')
print(f'AUMENTANDO 10%, TEMOS {funções108.moeda(funções108.aumentar(p, 10))}')
print(f'DIMINUINDO 13%, TEMOS {funções108.moeda(funções108.diminuir(p, 13))}')