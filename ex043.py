from math import pow

peso = float(input('diga seu peso: '))
altura = float(input('diga sua altura'))
imc = peso / pow(altura, 2)
print(f'seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 30:
    print('sobrepeso')
elif 30 <= imc < 40:
    print('obesidade')
else:
    print('obesidade mórbida')