n = input("Digite algo a seguir: ")

print("O tipo primitivo desse valor é {}, Só tem espaços? {}, é um numero?{}, é alfabético?{}, é alfanumérico?{}, está em maiúscula?{}, Esta em minusculas?{}, está capitalizado?{}".format(type(n), n.isspace(), n.isnumeric(), n.isalpha(), n.isalnum(), n.isupper(), n.islower(), n.istitle()))





print("Só tem espaços?", n.isspace())
print("É um número?", n.isnumeric())
print("É alfabético?", n.isalpha())
print("É alfanumérico?", n.isalnum())
print("Está em maiúsculas?", n.isupper())
print("Está em minusculas?", n.islower())
print("Está capitalizada?", n.istitle())