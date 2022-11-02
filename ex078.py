num = []
for c in range(0,5):
    num.append(int(input(f'digite um número para a posição {c}: ')))
maior = max(num)
menor = min(num)
print('-='*20)
print(f'os números digitados foram {num}: '.upper())
print('-='*20)
print(f'O maior valor digitado foi {maior} em posição: ', end='')
for pos, intem in enumerate(num):
    if maior == intem:
        print(f'{pos}', end=' ')
print(f'\nO menor valor digitado foi {menor} em posição: ', end='')
for pos, intem in enumerate(num):
    if menor == intem:
        print(f'{pos}', end=' ')