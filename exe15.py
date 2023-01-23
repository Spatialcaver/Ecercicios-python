#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km= float(input('quantos km o veículo percorreu? '))
dias = float (input('Por quantos dias o veiculo foi alugado? '))
total = (dias*60.00)+(km*0.15)

print('o Valor total a pagar é de R$ {:.2f} '.format(total))