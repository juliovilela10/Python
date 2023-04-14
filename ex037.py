numero = int(input('\033[32mDigite um número inteiro\033[m: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
opção = int(input('\033[34mSua opção\033[m: '))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')
