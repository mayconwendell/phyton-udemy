#Escreva um programa que faça o computador "pensar" em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
#escolhido pelo computador

#O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import choice

nu = [0, 1, 2, 3, 4, 5]

n = choice(nu)

chute = int(input("Digite um número para tentar acertar: "))

if chute == n:
    print(f'O número escolhido foi {chute}, e o correto é {n} Parabéns, você venceu!')
else:
    print(f'O número escolhido foi {chute}, e o número correto é {n}, Infelizmente você perdeu')