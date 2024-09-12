nome = input("Qual o seu nome? ")

if nome == "Maycon":
    print('Olá Maycon, seja muito bem-vindo na nossa instituição')
else:
    print(f'Olá {nome}, Espero que goste da nossa intituição')

#-------------------------------------------------------------------
namorada = input('Digite seu nome completo: ').strip().lower()

if namorada == 'samara neri ferreira':
    print('Eu te amo meu amor, to com saudades de ti já <3')
else:
    print('Oq que você está fazendo aqui? Ele so tem olhos pra mulher dele')

#-----------------------------------------------------------------------

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
n3 = float(input("Digite a sua terceira nota: "))

m = (n1 + n2 + n3) /3

if m >=7.0:
    print(f'Você teve a média de {m:.1f}, PARABENS VOCÊ FOI APROVADO!')
else:
    print(f"Você teve a média de {m:.1f}, Infelizmente terá que fazer a recuperação, estude mais!" )