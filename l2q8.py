'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''
#entrada
valor_1 = float(input('Digite o valor do primeiro pruduto: '))
valor_2 = float(input('Digite o valor do segundo produto: '))
valor_3 = float(input('Digite o valor do terceiro produto: '))

#processamento
if valor_1<valor_2 and valor_3:
#saída
    print('O produto mais brarato é o primeiro produto')
elif valor_2<valor_3:
#saída
    print('O produto mais barato é o segundo produto')
else:
#saída
    print('O produto mais barato é terceiro produto')
