# Conversor de Bases númericas

print('CONVERSOR DE BÁSES NÚMERICAS')

num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para converção. 
[1] BINÁRIO
[2] ÓCTAL
[3] HEXADECIMAL ''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('O número {} convertido para BINÁRIO é {}' .format(num, bin (num) [2:] ))
elif opção == 2:
    print('O número {} convertido para OCTAL é {}' .format(num, oct(num) [2:] ))
elif opção == 3:
    print('O número {} convertidopara HEXADECIMAL é {}' .format(num, hex(num) [2:] ))
else:
    print('OPÇÃO INVALIDADE. TENTE NOVAMENTE')
        