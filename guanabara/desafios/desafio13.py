#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo 
#salário, com 15% de aumento.

salario = int(input("Digite seu salário: "))

aumento = salario*(15/100)

print("Seu salário era de {} e agora você vai passar a receber ".format(salario), end="")
print("{} graças ao dissidio retroativo".format(salario+aumento))