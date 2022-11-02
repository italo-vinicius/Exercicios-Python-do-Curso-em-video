# def area():
#     l = float(input('LARGURA (M): '))
#     c = float(input('COMPRIMENTO (M): '))
#     print(f'A ÁREA DO TERRENO {l:.2f}x{c:.2f} FOI {l * c:.2f}m²')

# print('CONTROLE DE TERRENOS')
# print('-='*15)
# area()

def area(larg, comp):
    a = larg * comp
    print(f'A ÁREA DO TERRENO {larg}x{comp} FOI {a}m²')



print('CONTROLE DE TERRENOS')
print('-='*15)
l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO (M): '))

area(l, c)