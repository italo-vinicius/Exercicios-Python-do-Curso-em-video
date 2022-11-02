resp = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while resp in 'S':
    leitor = int(input('digite um número inteiro: '))
    cont += 1
    soma += leitor
    if cont == 1:
        maior = leitor
        menor = leitor
    else:
        if leitor > maior:
            maior = leitor
        if leitor < menor:
            menor = leitor
    resp = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()[0]
media = soma / cont
    
print(f'A MÉDIA ENTRE TODOS OS NÚMEROS DIGITADOS FOI {media:.2f}\nO MAIOR NÚMERO FOI {maior} E O MENOR FOI {menor}')