#faça um programa que leia um  valor em Metros e mostre seu valor em centimetros e milimetros

valor=float(input('Informe um valor em Metros: '))
cen = valor*100
mili= valor*1000

print('o valor {} em metros corresponde a: {:.2f} em centimetros, e a: {:.2f} em milimetros.'.format(valor,cen,mili))