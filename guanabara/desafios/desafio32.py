#Faça um programa que leia um ano qualquer e mostre se ele é Bissexto 

ano = int(input("Digite um ano para ver se ele é bissexto: "))

if ano %4==0:
    print(f"O ano digitado é {ano}, e sim esse ano é bissexto!")
else:
    print(f"O ano digitado é {ano}, e esse ano não é bissexto!")