#Crie um programa que leia quanto tem na carteira e mostre
#Quantos dólares ela pode comprar

reais = float(input("Quantos reais você tem:"))

dolar = 3.27

if reais ==3.27:
    print("Você pode comprar US$ 1.00.")

elif reais >=3.27:
    print("Você pode comprar US$ {:.10}, e sobra {:.2}".format(reais/dolar, reais%dolar)) 
else:
    print("Você não tem saldo suficiente para adiquirir dólares")