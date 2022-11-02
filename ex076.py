listinha = ('PARCELA DO PC: ', 'R$542', 'MANUTENÇÃO DO APARELHO: ', 'R$90', 'ALUGUEL: ', 'R$700')
for c in range(0, len(listinha), 2):
    print(f"{listinha[c]:<25}" + f'{listinha[c + 1]}')
