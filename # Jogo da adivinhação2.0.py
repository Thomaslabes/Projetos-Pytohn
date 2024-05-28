# Jogo da adivinhação2.0

from random import randint
computador = randint(0,50)

print('-=' * 20)
print('Sou seu computador...Acabei de pensar em um número aléatorio Thomas')
print('Será que você consegue adivinhar qual foi? ')
print('-=' * 20)

nome = input('Qual o seu nome ? ')

acertou = False
palpites = 0

from time import sleep

while not acertou:
    jogador = int(input(' Qual é o seu palpite ? '))
    print('PROCESSANDO...')
    sleep(1)
    palpites += 1 
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Esta frio. ')
        elif jogador > computador:
            print(' Menos... Esta quente. ')
   
print('Você acertou com {} tentativas {} '.format(palpites, nome))

resposta= str(input('Deseja tentar mais uma vez ? '))
if resposta == 'sim':
    print('Ok!')
else:
    print('FIM')