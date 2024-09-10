#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo 
#salário, com 15% de aumento.

salario = float(input("Digite seu salário: "))

aumento = salario + (salario*15/100)

print("Seu salário era de {:.2f} e agora você vai passar a receber ".format(salario), end="")
print("{:.2f} graças ao dissidio retroativo".format(aumento))


#Faça um algoritmo que leia o preço de um produto e mostre seu novo 
#valor, com 15% de desconto, caso seja parcelado o valor será aumentado
#em 10% do valor normal

valor = float(input("Qual o valor do produto que deseja consultar: "))

desc = valor - (valor * 15/100)
parc = valor + (valor * 10/100)

print("O valor do produto é de R${:.2f}, caso pague à vista o valor será de R${:.2f}".format(valor, desc))
print("caso parcele o valor, sera acrescido 10%, ficando R${:.2f}".format(parc))

#Faça um algoritmo que leia dois valor de dois produtos e diga para o cliente o mais barato

p1 = float(input("Digite o valor do primeiro produto: "))
p2 = float(input("Digite o valor do segundo produto: "))

if p1 > p2:
    print("O produto 1 que está R${} sai mais em conta que o produto dois que está R${}, se você pretende gastar menos, é a melhor opção".format(p1, p2))
else:
    print("O produto 2 que está R${} está mais em conta que o produto 1 que está R${}, se pretende gastar pouco, é a melhor opção.".format(p2, p1))
    