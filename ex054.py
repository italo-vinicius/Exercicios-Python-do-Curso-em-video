from datetime import date
maiores = 0
menores = 0
for c in range(1, 8):
    ano = int(input('digite seu ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f'{maiores} são maiores de idade. {menores} são menores')