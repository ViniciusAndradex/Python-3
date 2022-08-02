def soma(a, b):
    print(f'A = {a} e B = {b}')
    print(a + b)


def soma1(* num):
    s = 0
    for c in num:
        s += c
    print(f'Soma = {s}')


def contador(*num):
    print(num)


def lin():
    print('-' * 30)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa Principal
lin()
soma(a=4, b=5)
soma(b=8, a=9)
soma(2, 1)
lin()
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
lin()
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
lin()
soma1(1, 2, 3)
soma1(1, 2, 4, 1)
