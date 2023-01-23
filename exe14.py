#faça um algoritimo que receba um valor em C° para F°

temp = float(input('informe um valor em graus C°: '))
conv=(temp*9/5)+32
print('o valor em C° {:.2f} convertido para a escala F° é {:.2f}'.format(temp,conv))