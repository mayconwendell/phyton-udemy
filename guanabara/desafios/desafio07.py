#Desenvolva um programa que leia as duas notas de um aluno, calcula
#E mostra a sua média.

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))

media = (n1 + n2 + n3) /3

#Utilizei :.2 para dizer que eu quero que apareça somente duas casas decimais
print("A media do aluno no semestre foi de {:.2}".format(media))