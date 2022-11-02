times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense',
'Atlético','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória',
'Curitiba','Avaí','Ponte preta','Atlético-GO')

print(f'\033[1;32mOS 5 PRIMEIROS TIMES SÃO:\033[m {times[:5]}')
print(f'\033[1;31mOS 4 ÚLTIMOS SÃO:\033[m {times[-4:]}')
print(f'\033[1;33mTIMES EM ORDEM ALFABÉTICA:\033[m {sorted(times)}')
print(f'\033[1;34mO CRUZEIRO ESTÁ NA POSIÇÃO {times.index("Cruzeiro")}\033[m ')