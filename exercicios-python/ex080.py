lista = list()
for item in range(0, 5):
    num = int(input('Digite um número: '))
    if item == 0 or num > lista[-1]:
        print('Adicionado ao final...')
        lista.append(num)
    else:
        for pos, c in enumerate(lista):
            if c > num:
                print(f'Adionado na posição {pos} da lista...')
                lista.insert(pos, num)
                break
print(lista)
