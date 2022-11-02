print('-' * 100)
print('EMPRÉSTIMOS PYTHON LTDA')
print('-' * 100)

vc = float(input('QUAL O VALOR DA CASA QUE VOCÊ QUER COMPRAR? '))
s = float(input('QUAL O SEU SALÁRIO? '))
t = int(input('EM QUANTOS ANOS VOCÊ QUER PAGAR? '))
meses = t * 12
p = vc / meses
if p <= s * 0.3:
    print(f'PARABÉNS. SEU EMPRÉSTIMO FOI APROVADO. A PARCELA SERÁ DE {p:.2f}')
elif p >= s * 0.3:
    print('POXA, INFELIZMENTE SEU EMPRÉSTIMO FOI NEGADO')