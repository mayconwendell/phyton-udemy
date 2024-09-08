#Faça um programa que leia a largura e a altura de uma parede em metros
#calcule a sua área e a quantidade de tinta necessária para pintar-la
#sabendo que cada litro de tinta, pinta uma área de 2m quadrados

largura = int(input("Digite a largura da sua parede: "))
altura = int(input("Digite a altura da sua parede: "))

area = largura*altura
tinta = 2

print("A área da sua parede é de {}, você ".format(area), end="")
print("precisa de {} litros de tinta para pinta-la".format(area/tinta))