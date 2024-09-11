#Crie um programa que leia o nome de uma pessoa e diga se ela tem 
#"SILVA" no nome.

n = input("Digite o seu nome completo: ").strip()

print(f"Seu nome tem Silva? {'silva' in n.lower()}")
