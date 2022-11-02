from datetime import date
d = int(input('DIGITE SEU ANO DE NASCIMENTO:'))
i = date.today().year - d
if i < 18:
    print(f'VOCÊ AINDA NÃO PODE SE ALISTAR. FALTAM {18 - i} ANOS PARA SE ALISTAR!!!')
elif i > 18:
    print(f'VOCÊ ESTÁ APTO PARA SE ALISTAR FAZ {i - 18} ANOS!!!')
else:
    print('VOCÊ TEM 18 ANOS E JÁ PODE SE ALISTAR.\033[1;31CORRA!!!')