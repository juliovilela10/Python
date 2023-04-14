n1 = float(input('\033[32mPrimeira Nota\033[m: '))
n2 = float(input('\033[32mSegunda Nota\033[m: '))
media = (n1 + n2) / 2
print('Sua media foi {:.1f}:'.format(media))
if media >= 7:
    print('\033[34mParabens você foi APROVADO!\033[m')
elif media < 5:
    print('\033[31mVocê foi REPROVADO!\033[m')
else:
    print('\033[33mVocê está de RECUPERAÇÃO!\033[m')
