# Maior e Menor

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Analisa qume é o menor <
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c


# Ánalisa quem é o maior >
maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi o {}' .format(menor))
print('O maior valor digitado foi o {}' .format(maior))