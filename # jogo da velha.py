# jogo da velha

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('BEM VINDO AO JOGO DA VELHA!!!')

print('''Escola suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')


jogador = int(input('Qual sua jogada? '))

print('JO')
sleep(1)

print('KEN')
sleep(1)

print('PÔ')
sleep(1)

print('-=' *15)
print('Computador pensou em {}' .format(itens[computador]))
print('O jogador pensou em {}' .format(itens[jogador]))
print('-=' * 15)

if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('Você VENCEU!')
    
    elif jogador == 2:
        print('Você PERDEU!')
    
    else:
        print('OPÇÃO INVÁLIDA') 

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('Você PERDEU!')
    
    elif jogador == 1:
        print('EMPATE')
    
    elif jogador == 2:
        print('Você VENCEU!')
    else:
        print('OPÇÃO INVÁLIDA')

elif computador == 2: #COMPUTADOR JOGOU TESOURA
        
    if jogador == 0:
        print('Você GANHOU!')
    
    elif jogador == 1:   
        print('Você PERDEU!')
    
    elif jogador == 2:
        print('EMPATE!')
    
    else:
        print('OPÇÃO INVÁLIDA')