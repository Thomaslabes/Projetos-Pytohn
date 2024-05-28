# Progressão aritmética 2.0

print('GERADOR DE PA')
print('-=' * 12)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

termo = primeiro 
cont = 1

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1

