#faça um algoritimo que peça o valor de um produto e mostre seu valor com 5% de desconto.

valor=float(input('Informe o valor do produto: '))
taxa= 5.00
desconto = valor*taxa/100
total= valor-desconto
print('o produto que custava R${:.2f}, agora custa R${:.2f} com desconto de 5%! '.format(valor, total))