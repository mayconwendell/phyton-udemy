#Crie um programa que converta uma temperatura dada em graus Celsius 
#Para fehrenheit.

c = float(input("Digite a Quantidade de Graus: "))

f = c * 1.8 +32

print("A conversão de {:.1f} graus para fahrenheit é de {:.1f}".format(c, f))