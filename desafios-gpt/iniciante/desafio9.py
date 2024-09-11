#Crie um programa que peça ao usuário três números e exiba a 
#media deles

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

m = (n1 + n2 + n3) /3

print(f"A soma dos números {n1}, {n2} e {n3} da a média {m:.1f}")