#Faça um programa que leia um ângulo qualquer e mostre 
#na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, radians, cos, tan

ang = float(input("Digite um ângulo qualquer: "))

conv = radians(ang)

sen = sin(conv) 
cos = cos(conv)
tan = tan(conv)

print(f"O ângulo é {ang:.2f}, o seno é {sen:.2f}, o cosseno é {cos:.2f} e a tangente é {tan:.2f}")

