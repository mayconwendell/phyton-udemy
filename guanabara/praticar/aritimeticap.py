n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))

soma = n1 + n2
multi = n1 * n2
divisao = n1 / n2
inteira = n1 // n2
pote = n1 ** n2 
resto = n1 % n2

print("O valor do resultado somado é de {}, da multiplicação {}, ".format(soma, multi), end="")
print("da divisão {}, divisão inteira {}, potência {}, resto da divisão {}.".format(divisao, inteira, pote, resto))

print("O valor da soma é de", soma, "da multiplicação é de", multi)