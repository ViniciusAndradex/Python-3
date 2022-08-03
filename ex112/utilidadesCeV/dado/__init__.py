def leiaDinheiro(num):
    while True:
        x = input(num)
        x = x.replace(',', '.')
        teste = x.replace('.', '').isdigit()
        if teste:
            num = float(x)
            break
        else:
            print(f'\033[1;31mERRO: \"{x}\" é um preço inválido!\033[m')
    return num
