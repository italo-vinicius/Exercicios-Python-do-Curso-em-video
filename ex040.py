n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = n1 + n2 / 2
if m < 5:
    print('REPROVADO')
elif 5 <= m <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')