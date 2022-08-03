def leiaDinheiro(num):
    while True:
        x = input(num)
        if x.isnumeric():
            num = float(x)
            break
        else:
            print(f'\033[1;31mERRO: \"{x}\" é um preço inválido!')
    return num
