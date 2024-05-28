# Aula 14

n = 1
par = impar = 0
while n != 0:
    n = int(input(' Digigte um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} número(s) pares e {} número(s) impares!' .format(par, impar))