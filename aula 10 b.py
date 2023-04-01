n1=float(input('Digite a Primeira Nota: '))
print('-'*20)
n2=float(input('Digite a Segunda Nota: '))
print('-'*20)
m= (n1+n2)/2
print('Parabéns' if m>= 6 else'STUDE MAIS!')# Condição simplificada
print('Sua média foi: {:.1f}'.format(m))
print('-'*20)
if m>=7.0:
    print('Você Foi Aprovado!!\nBoas Férias!')
    print('='*20)
else:
    print('Você está de Exame!\nProcure a Secretaria.\n')