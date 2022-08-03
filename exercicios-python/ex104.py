def leiaInt(num):
    show = False
    while not show:
        x = input(num)
        if not x.isnumeric():
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            num = int(x)
            show = True
    return num


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar, o número {n}')
