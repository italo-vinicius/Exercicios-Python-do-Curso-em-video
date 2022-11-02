frase = str(input('digite uma frase: ')).upper().strip()
print(f'a letra A aparece {frase.count("A")} vezes')
print(f'a palavra A aparece pela primeira vez na posição {frase.find("A")+1}')
print(f'a palavra A aparece pela última vez na posição {frase.rfind("A")+1}')