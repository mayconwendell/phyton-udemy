#Escreva um programa que leia um valor em metros e o exiba convertido
#em centímetros e milímetros

metro = int(input("Digite a quantidade de metros: "))

centimetro = metro * 100
milimetro = metro * 1000

print("A Quantidade de metros escolhida foi de {}, isso da {} em centimetros, ".format(metro, centimetro), end="")
print("e {} em milimetros".format(milimetro))