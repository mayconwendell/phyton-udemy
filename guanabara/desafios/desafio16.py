#Crie um programa que leia um número real qualquer pelo teclado e mostre
#na tela a sua porção inteira. EX: 6.127 = 6

from math import trunc
n = float(input("Digite um número real: "))

inteiro = trunc(n)

print(f"O Número real é {n} e a versão inteira desse número é {inteiro}")