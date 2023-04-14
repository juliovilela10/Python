print('\033[32m-=\033[m' * 20)
print('\033[0;31;40mAnalisandor de Triângulos\033[m')
print('\033[32m-=\033[m' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo! ')
else:
    print('Os segmentos acima não PODEM FORMAR um triângulo! ')
