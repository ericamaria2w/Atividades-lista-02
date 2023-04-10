#18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dia = int(input('Digite um dia: '))
mes = int(input('Digite um mês: '))
ano = int(input('Digite um ano: '))

if dia <= 31:
    print('Esse dia é válido!') 
if mes <=12:
    print('Esse mês é válido!')
if ano <=2023:
    print('Esse ano é válido')

print(f'Então o dia {dia}/{mes}/{ano} é válido!!')