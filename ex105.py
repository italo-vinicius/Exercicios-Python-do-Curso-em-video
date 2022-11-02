def notas(*nota, sit=False):
    """
    exemplo docstring..
    use help(notas)
    """
    dados = {}
    dados['TOTAL'] = len(nota)
    dados['MAIOR'] = max(nota)
    dados['MENOR'] = min(nota)
    media = sum(nota) / len(nota)
    dados['MÉDIA'] = (f'{media:.2f}')
    if sit:
        if media >= 7:
            dados['SITUAÇÃO'] = 'SOSSEGADOS'
        elif 5 <= media <7:
            dados['SITUAÇÃO'] = 'TENSO..BORA ESTUDAR'
        else:
            dados['SITUAÇÃO'] = 'FERRADOS'
    return dados

resp = notas(1,4,6,7,3,2,9, sit=True)
print(resp)
