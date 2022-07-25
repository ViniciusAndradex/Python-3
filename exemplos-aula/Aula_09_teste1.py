frase = 'Curso em Video Python'
print(frase)
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('O'))
print(frase.count('o')) #Case sensitive
print(frase.upper().count('O'))
print(len(frase))

frase = ('   Curso em Video Python   ')
print(frase.strip())
print('-'.join(frase))
print(frase.replace('Python', 'Android'))
print(frase.split())

frase = 'Curso em Video Python'
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('curso'))
print(frase.lower().find('curso'))
div = frase.split()
print(div[2][3])
