v = float(input('digite a velocidade do carro: '))
m = (v - 80) * 7
if v > 80:
    print(f'o carro estava acima da velocidade permitida e será multado em {m:.2f}R$!!!')
else:
    print('o carro estava em uma velocidade permitida')
