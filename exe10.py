#crie um programa que pergunte quanto o user tem em R$ na carteira e diga quanto em dolar ele pode comprar em U$:

carteira= float(input('informe quanto você tem na carteira em R$? '))
dolar= 3.27

print('com R${:.2f}, você pode comprar U${:.2f} '.format(carteira, carteira/dolar))