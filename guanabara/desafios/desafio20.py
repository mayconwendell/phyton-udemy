#O mesmo professor do desafio anterior quer sortear a ordem de
#trabalhos dos alunos. Faça um programa que leia o nome dos
#quatro alunos e mostre a ordem sorteada.

import random

a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")

li = [a1, a2, a3, a4]
st = random.shuffle(li)

print("A ordem de apresentação dos trabalhos escolhida foi:")
print(li)