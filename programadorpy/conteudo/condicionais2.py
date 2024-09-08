#elif = else if (ou então)

salario = float(input("Informe seu salário:"))

if salario <= 3000:
    print("programador junior")
elif salario > 3000 and salario <=6000:
    print("programador senior")
elif salario > 6000 and salario <=15000:
    print("programador senior")
else:
    print("gerente de projetos")