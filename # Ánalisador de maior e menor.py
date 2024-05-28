# Ánalisador de maior e menor 

from datetime import date 
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 5):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1 
print ('Ao todo tivemos {} pessoas maiores de idade' .format(totmaior))
print('E tivemos {} pessoas de menor'. format (totmenor))