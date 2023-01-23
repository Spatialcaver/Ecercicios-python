# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
alu01=input('insira o nome do primeiro aluno: ')
alu02=input('inra o nome do proximo aluno: ')
alu03=input('insira o nome do proximo aluno: ')
alu04=input('insira o nome do ultimo aluno: ')
lista=[alu03,alu02,alu01,alu04]
print('=' * 20)
print('o aluno escolhido foi:', random.choice(lista))
print('=' * 20)