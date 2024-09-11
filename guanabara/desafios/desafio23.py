# Faça um programa que leia um número de 0 a 9999 e 
# mostre na tela cada um dos dígitos separados.


#Versão fazendo um número virar uma string
n = int(input("Digite um número de 1 à 4 digitos: "))

num = str(n)

print(f'Analisando o número {n}')
print(f'A unidade dele é {num[3]}')
print(f'A dezena dele é {num[2]}')
print(f'A centena dele é {num[1]}')
print(f'E o Milhar é {num[0]}')

#Versão de números
nu = int(input("Digite um número: "))

u = nu // 1 % 10
print(f"A Unidade do número é {u}")

d = nu // 10 % 10
print(f"A Dezena desse número é {d}")

c = nu // 100 % 10 
print(f"A Centena desse número é {c}")

m = nu // 1000 % 10
print(f"O Milhar desse número é {m}")