frase = 'Curso em video Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2])
print('oi')

print("""Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().""")

print(len(frase))
frase.replace('Curso','Nico')
print('Curso' in frase)
print(frase.lower().find('Video'))

print(frase.split())

divi=frase.split()

print(divi[2][3])