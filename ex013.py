sal = float(input('Qual é o seu salário? R$'))
aum = sal + (sal * 15 / 100)
print('Seu salário é de R${:.2f}, como aumento de 15% seu novo salário é R${:.2f}'.format(sal, aum))
