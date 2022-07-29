lista = list()
for item in range(0, 5):
    num = int(input('Digite um número: '))
    if item == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final...')
    else:
        for pos, c in enumerate(lista):
            if c > num:
                lista.insert(pos, num)
                print(f'Adionado na posição {pos} da lista...')
                break
print(lista)
