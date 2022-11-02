somaidade = 0
idademaisvelho = 0
nomemaisvelho = ''
totalmulher20 = 0
for c in range(1, 5):
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = int(input('DIGITE 1 PARA MASCULINO OU 2 PARA FEMININO: '))
    if c == 1 and sexo == 1:
        idademaisvelho = idade
        nomemaisvelho = nome
    if sexo == 1 and idade > idademaisvelho:
        nomemaisvelho = nome
    if sexo == 2 and idade < 20:
        totalmulher20 += 1
    somaidade += idade
mediaidade = somaidade / 4
print(f'O HOMEM MAIS VELHO É {nomemaisvelho}, A MÉDIA DE IDADE DAS PESSOAS É {mediaidade} E TEM {totalmulher20} MULHERES MENORES DE 20 ANOS')