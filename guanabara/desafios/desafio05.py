#Faça um programa que leia um número inteiro e mostra na tela o seu 
#sucessor e seu antecessor 

n1 = int(input('Digite um Número:'))

ant = n1 - 1
sus = n1 + 1

print("O Numero é {}, O seu Antecessor é {}, E o seu Sucessor é {}".format(n1, ant, sus))