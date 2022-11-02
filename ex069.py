maior18 = 0
homenscadastrados = 0
mulheresmenos20 = 0
while True:
    sexo = ' '
    idade = int(input('IDADE: '))
    while sexo not in 'FM':
        sexo = str(input('SEXO: [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homenscadastrados += 1
    if idade < 20 and sexo == 'F':
        mulheresmenos20 += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('QUER CONTINUAR? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'{maior18} pessoas tem mais de 18 anos')
print(f'{homenscadastrados} homens foram cadastrados')
print(f'{mulheresmenos20} mulheres tem menos de 20 anos')