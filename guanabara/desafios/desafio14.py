#Escreva um programa que converta uma temperatura digitada em ºC e a converta para ºF.

temp = float(input("Informe a temperatura em ºC: "))

fh = temp * 1.8 + 32

print("Convertendo a temperatura de ºC para fahrenheit, a resposta é {:.2f}".format(fh))