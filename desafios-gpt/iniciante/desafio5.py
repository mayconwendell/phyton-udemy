#Escreva um programa que peça ao usuário uma string e 
#retorne essa string invertida.

def inverter_string(texto):
    return texto[::-1]

# Exemplo de uso
texto = input("Digite uma string: ")
resultado = inverter_string(texto)
print(f"A string invertida é: {resultado}")