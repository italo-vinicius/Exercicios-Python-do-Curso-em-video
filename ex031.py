d = float(input('digite a distância da viagem: '))
if d <= 200:
    print(f'a viagem custará {d * 0.50}R$')
else:
    print(f'a viagem custará {d * 0.45}R$')