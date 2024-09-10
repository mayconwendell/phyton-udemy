#Crie um programa que receba um número do usuário e determine se ele
#é par ou é impar

n = int(input("Digite aqui o número: "))

if n%2==0:
    print("O Número que você escolheu foi {}, e esse número é par".format(n))
else:
    print("O número que você escolheu foi {} e esse número é impar".format(n))    