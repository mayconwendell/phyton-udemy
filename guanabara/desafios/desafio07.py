#Desenvolva um programa que leia as duas notas de um aluno, calcula
#E mostra a sua média.

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))

media = (n1 + n2 + n3) /3

#Utilizei :.1f para dizer que eu quero que apareça somente uma 
#casa decimal flutuantes(após o ponto).
print("A media do aluno no semestre foi de {:.1f}".format(media))