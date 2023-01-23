#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo=float(input('digite o  valor do ângulo: '))
conv=math.radians(angulo)
seno=math.sin(conv)
tangente=math.tan(conv)
cos=math.cos(conv)
print('dado o valor de {} para o ângulo temos os seguintes valores: '.format(angulo))
print('=' * 10)
print('o seno é igual a: {:.2f}'.format(seno))
print('o coseno é igual a: {:.2f}'.format(cos))
print('A tangente é igual a: {:.2f}'.format(tangente))
