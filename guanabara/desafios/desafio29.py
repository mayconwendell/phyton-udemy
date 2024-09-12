#Escreva um programa que leia a velocidade de um carro.

#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

#A multa vai custar 7,00 por cada Km acima do limite

km = float(input("Digite quantos Km/h você estava dirigindo: "))

multa = 7 * (km%80)

if km >80:
    print(f'Você estava andando à {km} Km/h, você foi multado em {multa:.1f}')
else:
    print(f'Você estava andando à {km} Km/h, continua se policiando no volante!')