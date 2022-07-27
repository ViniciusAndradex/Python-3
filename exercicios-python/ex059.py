menu = 0
n = int(input('Digite um valor: '))
n1 = int(input('Digite outro valor: '))
while menu != 5:
    menu = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
- '''))
    print('-*-' * 10)
    if menu == 1:
        print(f'{n} + {n1} = {n + n1}')
    elif menu == 2:
        print(f'{n} * {n1} = {n * n1}')
    elif menu == 3:
        if n > n1:
            print(f'{n} é maior que {n1}')
        elif n1 > n:
            print(f'{n1} é maior que {n}')
        else:
            print(f'Ambos são {n}')
    elif menu == 4:
        print('Informe novamente os números:')
        n = int(input('Digite um valor: '))
        n1 = int(input('Digite outro valor: '))
    elif menu == 5:
        print('Thanks for using the app!')
    else:
        print('\033[1;31mOpção Inválida!!\033[m')
    print('-*-' * 10)
