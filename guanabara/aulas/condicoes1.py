tempo = int(input("Quantos anos tem seu carro? "))

if tempo >= 10:
    print("Seu carro já tem bastante tempo de uso, se possível troca-lo")
else:
    print("Seu carro está inteirissimo!")

#Condição simplificada

t = int(input("Digite quantos anos tem seu carro? "))

print('carro novo' if tempo <=3 else 'carro velho')

print('--FIM--')