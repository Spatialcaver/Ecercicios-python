# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
n1=input('digite o nome do primeiro aluno: ')
n2=input('digite o nome do segundo aluno: ')
n3=input('digite o nome do terceiro aluno: ')
n4=input('digite o nome do ultimo aluno: ')
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print('=' * 20)
print('a ordem de apresentação é : {}'.format(lista))
print('=' * 20)
