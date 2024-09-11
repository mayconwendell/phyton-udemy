#Faça um programa que leia uma frase pelo teclado e mostre 
# quantas vezes aparece a letra "A", em que posição ela aparece 
# a primeira vez e em que posição ela aparece a última vez.

f = input("Digite uma frase: ").upper().strip()

print(f"A letra A aparece {f.count("A")} vezes na frase")
print(f"A primeira letra a apareceu na posição {f.find("A")+1}")
print(f"A ultima letra a apareceu na posição {f.rfind("A")+1}")