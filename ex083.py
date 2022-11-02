express = [str(input('DIGITE UMA EXPRESSÃO: '))]
newlist = []
for c in express:
    if c == '(':
        newlist.append('(')
    elif c == ')':
        if len(newlist) > 0:
            newlist.pop()
        else:
            newlist.append(')')
            break
if len(newlist) == 0:
    print('EXPRESSÃO VÁLIDA')
else:
    print('EXPRESSÃO INVÁLIDA')