totalCompra = prodMaior1000 = maisBarato = 0
produtoMaisBarato = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$'))
    totalCompra += preco
    if preco > 1000.0:
        prodMaior1000 += 1
    if maisBarato == 0:
        maisBarato = preco
    else:
        if maisBarato > preco:
            maisBarato = preco
            produtoMaisBarato = produto
    while True:
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        print(f'{" FIM DO PROGRAMA ":-^30}')
        break
print(f'Total comprado: R$\033[1;35m{totalCompra:.2f}\033[m')
print(f'Produtos que valeram mais de R$1000.00: \033[1;34m{prodMaior1000}\033[m')
print(f'Produto mais barato: \033[1;31m{produtoMaisBarato}\033[m por R$\033[1;32m{maisBarato:.2f}\033[m')
