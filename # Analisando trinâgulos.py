# Analisando trinâgulos

print('-='* 18)
print(' Analisador de Triângulos')
print('-=' *18)

r1 = int(input('Primeiro ângulo : '))
r2 = int(input('Segundo ângulo : '))
r3 = int(input(' Terceiro ângulo : '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os ângulos podem formar um triângulo!' , end ='')

    if r1 == r2 == r3:
        print(' EQUILÁTERO ')
    
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO ')
     
    else:
        print(' ISÓELES ')

else:
    print('Os ângulos não podem formar um trinângulo! ')