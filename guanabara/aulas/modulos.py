#ceil - arredonda pra cima
#floor - arredonda para baixo
#trunc - 
#pow - potência
#sqrt - calcular raiz quadrada
#factorial - para fatorar número

import math

n = int(input("Digite um número: "))

raiz = math.sqrt(n)
fat = math.factorial(n)

#Usei o ceil para arredondar o número da raiz quadrada para cima.
print("O número é {}, a raiz desse número é {}\n e fat é {}".format(n, math.ceil(raiz)))


