#faça um programa que leia duas notas de um aluno e mostre sua média
n1=float(input('Informe sua primeira nota: '))
n2=float(input('Informe sua segunda nota: '))

media=(n1+n2)/2
if media > 6.5:
    print('Parabéns você foi aprovado com média: {}'.format(media))

else:
    print('Você está em recuperação sua media foi: {}'.format(media))
