preco = float(input('Preço: R$'))
menu = int(input('''\033[1;37;43mCONDIÇÕES DE PAGAMENTO\033[m
\033[1;34m[1] DINHEIRO/CHEQUE
[2] CARTÃO
[3] 2x CARTÃO
[4] 3x(+) CARTÃO
\033[1;34m- '''))
if menu == 1:
    totPagar = preco - (preco * 10 / 100)
elif menu == 2:
    totPagar = preco - (preco * 5 / 100)
elif menu == 3:
    totPagar = preco
    print(f'Sua compra será parcelada em 2x de R${totPagar / 2:.2f}')
elif menu == 4:
    totPagar = preco + (preco * 20 / 100)
    numParcela = int(input('Em quantas vezes?\n- '))
    print(f'Sua compra será parcelada em {numParcela}x de R${totPagar / numParcela:.2f}')
else:
    totPagar = preco
    print('OPÇÃO INVALIDA DE PAGAMENTO, TENTE NOVAMENTE!')
print(f'\033[1;30mTotal a pagar \033[1;31mR${totPagar:.2f}\033[m')
