#Escreva um programa que pergunte o salário de um funcionário e calcule
#o valor do seu aumento.

#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%

#Para os inferiores ou iguais, o aumento é de 15%

sal = float(input("Digite o valor para calcular seu aumento: "))

a1 = (sal * 10 / 100) + sal
a2 = (sal * 15 / 100) + sal

if sal > 1250:
    print(f"O seu salário é de {sal:.1f}, com o aumento de 10%, seu salário fica de R${a1:.1f}")
else:
    print(f"O seu salário é de {sal:.1f}, com o aumento de 15%, seu salário fica de R${a2:.1f}")
