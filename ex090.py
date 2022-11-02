aluno = dict()
aluno['nome'] = str(input('NOME: '))
aluno['média'] = float(input('MÉDIA: '))
print(f'SEU NOME É {aluno["nome"]} E SUA MÉDIA FOI {aluno["média"]}')
if aluno['média'] >= 7:
    print('PARABÉNS, VOCÊ FOI APROVADO. VOCÊ MERECE PIKA.')
else:
    print('BURRO DO KRL..REPROVADO..ESTUDE MAIS E LARGA O FREE FIRE')