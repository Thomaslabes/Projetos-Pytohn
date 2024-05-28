# Alistamento militar

from datetime import date

atual = date.today().year
nasc = int(input(' Em que ano você nasceu ?: '))
idade = atual - nasc
print(' Quem nasceu em {} tem {} anos em {}.' .format(nasc, idade, atual))

if idade == 18:
    print(' Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade 
    print(' Ainda faltam {} anos para o alistamento' .format(saldo))

elif  idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado a {} ano(s).' .format(saldo)) 