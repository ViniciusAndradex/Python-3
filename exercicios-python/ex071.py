while True:
    saque = int(input('Quanto deseja sacar? R$'))
    if saque > 50:
        notas = saque // 50
        if notas > 0:
            print(f'Total de {notas} cédulas de \033[1;31mR${50}\033[m')
        saque %= 50
        if saque != 0:
            notas = saque // 20
            if notas > 0:
                print(f'Total de {notas} cédulas de \033[1;32mR${20}\033[m')
            saque %= 20
            if saque != 0:
                notas = saque // 10
                if notas > 0:
                    print(f'Total de {notas} cédulas de \033[1;33mR${10}\033[m')
                saque %= 10
                if saque != 0:
                    if saque > 0:
                        print(f'Total de {saque} cédulas de \033[1;35mR${1}\033[m')
                    saque %= 1
    if saque == 0:
        break
print('-' * 40)
print('VOLTE SEMPRE AO BANCO CEV! Tenha um bom dia!')
