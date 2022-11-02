import funções109

p = float(input('DIGITE O PREÇO: R$'))
print(f'A METADE DE {funções109.moeda(p)} É {funções109.metade(p, True)}')
print(f'O DOBRO DE {funções109.moeda(p)} É {funções109.dobro(p, True)}')
print(f'AUMENTANDO 10%, TEMOS {funções109.aumentar(p, 10)}')
print(f'DIMINUINDO 13%, TEMOS {funções109.diminuir(p, 13)}')