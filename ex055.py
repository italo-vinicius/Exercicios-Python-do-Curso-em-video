#lista = []
#for c in range(1, 6):
#    peso = input(F'DIGITE O PESO DA PESSOA {c}: ')
#    lista += [peso]
#print(f'O MAIOR PESO FOI {max(lista)} E O MENOR FOI {min(lista)}')

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'PESO DA {p}ª PESSOA: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O MAIOR PESO É {maior} E O MENOR É {menor}')