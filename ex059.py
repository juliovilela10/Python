from time import sleep
n1 = int(input('Primeiro Valor:'))
n2 = int(input('Segundo Valor:'))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa''')
    opção = int(input('Qual é sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, multiplicar))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte Sempre!')
