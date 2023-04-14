somaid = 0
mediaid = 0
maioridhomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaid += idade
    if p == 1 and sexo in 'Mm':
        maioridhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridhomem:
        maioridhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaid = somaid / 4
print('A média de idade do grupo é de {} anos'.format(mediaid))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridhomem, nomevelho))
print('Ao todo são {} mulhers com menos de 20 anos'.format(totmulher20))
