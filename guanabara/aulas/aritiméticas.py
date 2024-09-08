# + adição, - subtração, * multiplicação, / divisão, **potência, 
# // divisão inteira, % resto da divisão

#ordem de precedência dos operadores sucessivamente
# 1- ()
# 2- ** potências
# 3- * multiplicação, / divisão, // divisão inteira, % resto da divisão
# No terceiro vai aparecer quem estiver primeiro no código.
# 4- Soma e subtração

print(122%3)
print(4**3)
print(19//2)

#Raiz quadrada
print(81**(1/2))

#Raiz cubica
print(127**(1/3))


nome = input('Qual o seu nome?')
print("Prazer em te conhecer {:-^20}!".format(nome))