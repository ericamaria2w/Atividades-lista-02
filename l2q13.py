'''13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''
dia = int (input('Digite o dia da semana em numero: '))
semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado' ,'Domingo')
if dia == 1:
    print('É Domingo')
elif dia == 2:
    print('È Segunda - Feira')
elif dia == 3:
    print('É Terça - Feira')
elif dia == 4:
    print('É Quarta - Feira')
elif dia == 5:
    print('É Quinta - Feira')
elif dia == 6:
    print('É Sexta - Feira')
elif dia == 7:
    print('É Sabado')
else :
    print('Dado inválido!')
