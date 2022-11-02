n1 = float(input('\033[1;32mdigite a primeira nota:\033[m '))
n2 = float(input('\033[1;31mdigite a segunda nota:\033[m '))
n3 = float(input('\033[1;34mdigite a terceira nota:\033[m '))
m = (n1 + n2 + n3) / 3
print(f'a \033[4mmédia\033[m do aluno é: \033[1;97;40m{m:.1f}\033[m')
