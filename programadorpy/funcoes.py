# a função nem sempre retorna algo para a aplicação.

def funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))

    resposta = funcao(valor1, valor2)

    print(valor1, "+", valor2, "=", resposta)