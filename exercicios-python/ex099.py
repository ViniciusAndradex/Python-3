from time import sleep


def lin():
    print('-=-' * 20)


def maior(* num):
    lin()
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        print(f'O maior valor informado foi {len(num)}.')
    else:
        print(f'O maior valor informado foi {max(num)}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
