#Crie um programa que leia um número inteiro e mostre na tela se é par
#ou impar

n = int(input("Digite um número: "))

if n %2==0:
    print(f"O número {n} é par")
else:
    print(f"O número {n} é impar")