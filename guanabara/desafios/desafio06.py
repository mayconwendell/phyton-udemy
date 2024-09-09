#Crie um algoritimo que leia um número e mostre o seu dobro, triplo 
#e a raiz quadrada

n1 = int(input("Escolha um número: "))

dobro = n1*2
triplo = n1*3
raiz = (n1**(1/2))

print("O Número escolhido foi {}, O dobro desse número é {}, O triplo é {}, ".format(n1, dobro, triplo), end="")
print("e a raiz quadrada é {:.2f},".format(raiz))

#É possível calcular a raiz quadrada usando pow
#EX

print("A raiz quadrada de {} é {}".format(n1, pow(n1,(1/2))))
