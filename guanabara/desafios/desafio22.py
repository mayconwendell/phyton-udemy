#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

n = input('Digite o seu nome: ').strip()

mai = n.upper()
print(f"O nome digitato todo maiúsculo fica {mai}")

mi = n.lower()
print(f"O nome digitado todo em minúsculo fica {mi}")

let = len(n)-n.count(' ')
print(f"O nome digitado tem {let} letras")

primeiro = n.find(' ')
print(f"O Seu primeiro nome tem {primeiro} letras")
