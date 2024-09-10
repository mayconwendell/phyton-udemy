#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo 
#que o carro custa R$60 por dia e R$ 0,15 por Km rodado.

dia = int(input("Quantos dias você utilizou o carro: "))
km = float(input("Quantos Km foram percorridos: "))

pago = (dia * 6) + (km * 0.15)

print("Você usou o carro por {} dias e rodou {:.1f} Km, o valor que você tem que pagar é de R${:.2f}".format(dia, km, pago))