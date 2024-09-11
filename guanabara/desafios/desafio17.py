#Faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triângulo retângulo, calcule
#e mostre o comprimento da hipotenusa. 

from math import sqrt

op = float(input("Digite o cateto oposto: "))
ad = float(input("Digite o cateto adjacente: "))

hip = sqrt(op**2 + ad**2)

print(f"A hipotenusa dessa equação é {hip:.2f}")