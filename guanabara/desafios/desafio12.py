#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço
#com 5% de desconto.

p1 = int(input("Digite o preço do produto: "))

desconto = p1*(5/100)

print("O desconto do produto no valor de {}, é de {}".format(p1, desconto))