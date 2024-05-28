# soma de pares 

soma = 0
cont = 0
for c in range(1, 3):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num 
        cont += 1


print('Voçê informou {} números PARES e a soma foi {}' .format(cont, soma))

