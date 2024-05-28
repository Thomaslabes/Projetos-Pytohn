# Conversos de Moedas
 
real = float(input('Quanto dinheiro você tem na carteira R$:'))
dolar =  real / 5.17
euro =  real / 5.62
print('Com {} R$ você consegue comprar US${:.2f}, E${:.2f}' .format(real, dolar, euro))
