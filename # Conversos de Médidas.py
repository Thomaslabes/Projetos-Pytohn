# Conversos de Médidas
medida = float(input( 'Distancia em metros:'))
km = medida / 1000 
hcm = medida / 100 
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm =  medida * 1000
print(' A converção de metros para km é {}, para hcm é {}, para dam é {}, para dm é {}, para cm é {}, e para mm é {}' .format(km, hcm, dam, dm, cm, mm))