#Crie um algoritimo que leia um número e mostre o seu dobro, triplo 
#e a raiz quadrada

n1 = int(input("Escolha um número: "))

print("O Número escolhido foi {}, O dobro desse número é {}, O triplo é {}, ".format(n1, n1*2, n1*3), end="")
print("e a raiz quadrada é {},".format(n1**1/2))