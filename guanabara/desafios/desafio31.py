#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de
#até 200Km a R$0,45 para viagens mais longas.

k = float(input("Digite quantos km foi a sua viagem: "))

km = 0.50 * k
lon = 0.45 * k

if k <=200:
    print(f"A sua viagem foi de {k:.2f}Km, o valor a ser pago é de R$ {km:.2f}")
elif k >200:
    print(f"O sua viagem foi arroz {k:.2f}Km, o valor a ser pago é de R${lon}")