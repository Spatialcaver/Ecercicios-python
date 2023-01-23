#crie um programa queleia um numero real e mostre na tela sua porção inteira
from math import ceil,floor
n=float(input('digite um valor em numeros reais e veja sua conversão em numero inteiro: '))
print('o valor digitado foi {}. e sua porção inteira para mais é {}, e para menos {}'.format(n,ceil(n), floor(n)))
