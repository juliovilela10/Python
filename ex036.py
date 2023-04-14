casa = float(input('\033[31mValor da casa\033[m: R$'))
salário = float(input('\033[31mSalário do comprador\033[m: R$'))
anos = int(input('\033[31mQuantos anos de financiamento\033[m? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar um casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('\033[32mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[31mEmpréstimo NEGADO!\033[m')
