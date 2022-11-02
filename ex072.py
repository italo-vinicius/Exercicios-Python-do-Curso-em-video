extenso = 'zero um dois três quatro cinco seis sete oito nove dez onze doze treze quartoze quinze dezesseis dezessete dezoito dezenove vinte'.split()
while True:
    n = int(input('digite um número entre 0 e 20: '))
    if n <= 20 and n >= 0:
        break
print(f'o extenso de {n} é {extenso[n]}')