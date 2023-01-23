#faça um algoritimo que leia o salario de um funcionario e mostre seu novo valor com um aumento de 15%

salario=float(input('informe o valor do seu saláro em R$'))
taxa = 15.0
aumento = (salario*taxa)/100
total= salario+aumento
print('Seu salario foi reajuastado em 15% no valor de R${:.2f}, totalizando R${:.2f}'.format(aumento,total))