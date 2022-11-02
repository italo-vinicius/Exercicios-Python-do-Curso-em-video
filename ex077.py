palavras = ('programe', 'amor', 'gata', 'ovo')
for p in palavras:
    print(f'\na palavra {p.upper()} tem as vogais:', end=' ')
    for letra in p:
        if letra in "aeiou":
            print(letra, end=' ')