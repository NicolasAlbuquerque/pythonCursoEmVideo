# Condições
tempo= int(input('Quantos anos tem seu carro?'))
print('Carro Novo'if tempo<=3 else 'Carro velho')
print('--fim--')


nome=str(input('Qual seu nome?')).strip().upper()
if nome== 'NICOLAS':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal.')
print('Bom dia, {}!'.format(nome.capitalize()))

