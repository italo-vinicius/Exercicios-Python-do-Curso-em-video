from datetime import date
def voto(n = 0):
    if n < 16:
        return print('VOCÊ AINDA NÃO PODE VOTAR')
    elif 16 <= n < 18 or n > 65:
        return print('VOTO OPCIONAL')
    else:
        return print('VOTO OBRIGATÓRIO')


for c in range(1, 6):
    anonasc = int(input('EM QUE ANO VOCÊ NASCEU? '))
    idade = date.today().year - anonasc
    voto(idade)