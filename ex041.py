from datetime import date
d = int(input('em que ano você nasceu?'))
idade = date.today().year - d
print(f'você tem {idade} e é um nadador ')
if idade <= 9:
    print('mirim')
elif 9 < idade <= 14:
    print('infantil')
elif 14 < idade <= 19:
    print('junior')
elif idade == 20:
    print('senior')
else:
    print('master')
