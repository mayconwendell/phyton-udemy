#Crie um programa que leia quanto tem na carteira e mostre
#Quantos dólares ela pode comprar

reais = float(input("Quantos reais você tem:"))

dolar = 3.27

euro = 6.16

if reais ==dolar:
    print("Você pode comprar US$ 1.00.")

elif reais >=dolar:
    print("Você pode comprar US$ {:.2f}, e sobra {:.2f}".format(reais/dolar, reais%dolar))
else:
    print("Você não tem saldo suficiente para adiquirir dólares")