# GERENCIADOR DE PAGAMENTOS

print (' {:=^40}' .format('LOJA TOMMY' ))

preço = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[1] à vista/cheque são 10% de desconto
[2] à vista no cartão (preço normal)
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é sua opção? '))

if opção == 1:
    total = preço - (preço * 10 / 100) 

elif opção == 2:
    total = preço - (preço * 10 / 100)

elif opção == 3:
    total = preço
    total = preço / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}' .format(preço))

elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas ?'))
 
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(preço, total))
