real = float(input('Quanto dinheiro você ten ba carteira? R$'))
dolar = real / 5.48
euro = real / 5.46
peso = real / 0.26
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar £{:.2f}'.format(real, euro))
print('Com R${:.2f} você pode comprar ${:.2f}'.format(real, peso))
