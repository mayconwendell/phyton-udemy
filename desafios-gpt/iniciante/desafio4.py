#Crie um programa que peça ao usuário um número e calcule o fatorial
#Desse número.

from math import factorial

n = int(input("Digite o número para ser fatorado: "))

fac = factorial(n)

print(f"O número {n} fatorado fica {fac}")



def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

numero = int(input("Digite um número para ser fatorado"))
resultado = calcular_fatorial(numero)
print(f"o resultado do número é {resultado}")
