    

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n = (n1 + n2 + n3)/3
print(' A sua média foi {:.2f}' .format(n))
if n >=6.0:
    print('PARABÉNS!!!')
else:
    print('Melhoras na próxima...')
