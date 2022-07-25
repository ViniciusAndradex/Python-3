frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A apareceu {frase.count("a")} na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("a") + 1}')
print(f'A ultima letra A apareceu na posição {frase.rfind("a") + 1}')
