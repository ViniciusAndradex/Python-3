def area(largura, comprimento):
    print(f'A área de um terreno {largura}x{comprimento} é de {largura * comprimento:.2f}m²')


# Programa Principal
print('CONTROLE DE TERRENOS')
print('-' * 20)
area(largura=float(input('Largura (m): ')), comprimento=float(input('COMPRIMENTO (m): ')))
