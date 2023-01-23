#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
catetoop=float(input('insira o valor do cateto oposto: '))
catetoadj=float(input('insira o valor do cateto adjacente: '))
potoop=math.pow(catetoop,2)
potadj=math.pow(catetoadj, 2)
soma=potadj+potoop
h = soma **(1/2)
print('a hipotenusa do triângulo digitado é igual a: {:.2f}'.format(h))
