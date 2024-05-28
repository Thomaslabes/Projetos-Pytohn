# JOGO DA ADIVINHAÇÃO 2.0

print('-=' * 15)
print('BEM VINDO AO JOGO DA ADIVINHAÇÃO')
print('Irei pensar em um número de 0 a 5.. tente adivinhar')
print('-=' *15)

nome = input('Digite seu nome: ')

from random import randint
from time import sleep

computador = randint (0,5)
jogador = int(input('Em que número pensei ? '))
print('PROCESSANDO...')
sleep (2)

if computador == jogador:
    print('Você me venceu. PARABÉNS!!!')

else:
    print('EU venci...Eu pensei no número {} e não no {}, mas sorte na proxíma {}' .format(computador, jogador, nome ))