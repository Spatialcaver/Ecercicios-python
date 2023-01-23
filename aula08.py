'''import math
num = int(input('insira um valor: '))
raiz = math.sqrt(num)

print ('a raiz quadarada de {}, é igual à: {} '.format(num, math.ceil(raiz)))
'''
from math import sqrt, ceil,floor
num = int(input('insira um valor: '))
raiz = sqrt(num)

print ('a raiz quadarada de {}, é igual à: {} '.format(num, ceil(raiz)))
