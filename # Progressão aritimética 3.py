# Progressão aritimética 3.0

print('GERADOR DE PA')
print('-=' * 10)

primeiro = int(input('Qual o primeiro termo ? '))
razão = int(input('Qual a razão ? '))
termo = 1 
cont = 1 
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM!')









