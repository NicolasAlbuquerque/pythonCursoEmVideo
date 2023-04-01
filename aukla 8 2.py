import math
num= int (input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}!'.format(num,raiz))
print('A raiz de {}  arredondada para cima é {}'.format(num, math.ceil(raiz)))
print ('A Raiz de {} arredondada para baixo é {}'.format(num,math.floor(raiz)))
