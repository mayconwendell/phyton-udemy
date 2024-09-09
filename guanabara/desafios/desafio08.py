#Escreva um programa que leia um valor em metros e o exiba convertido
#em centímetros e milímetros

m = float(input("Digite a quantidade de metros: "))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print("A medida de metros {} corresponde a \n{}km \n{}hm \n{}dam \n{:.0}dm\n{:.0}cm ".format(m, km, hm, dam, dm, cm), end="")
print("e {:.0}mm".format(mm))