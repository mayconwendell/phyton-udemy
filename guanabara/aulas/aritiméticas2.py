n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))

#Variáveis
soma = n1 + n2
m = n1 * n2 
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# \n serve para quebrar a linha. end serve para não quebrar a linha

print('A soma vale {}, \n o produto é {}, e a divisão é {:.3}'.format(soma, m, d), end='')
print("Divisão inteira {}, e a potência é {}".format(di, e))

