# Analisando Triângulo 

print('-='* 18)
print(' Analisador de Triângulos')
print('-=' *18)
r1 = float(input('Primeiro ângulo:'))
r2 = float(input('segundo ângulo:'))
r3 = float(input('terceiro ângulo:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
    print('Os segmentos acima podem formar um triângulo')
else:
    print(' Os segmentos acima não podem formar um triângulo')