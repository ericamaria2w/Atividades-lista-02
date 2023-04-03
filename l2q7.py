'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''
#entrada
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
#processamento
if numero1>numero2 and numero3:
#saída
    print('O número maior é {}'.format(numero1))
elif numero2>numero3:
#saída
    print('O número maior é {}'.format(numero2))
else:
#saída
    print('O número maior é {}'.format(numero3))

if numero1<numero2 and numero3:
#saída
    print('O menor número maior é {}'.format(numero1))
elif numero2<numero3:
#saída
    print('O número maior é {}'.format(numero2))
else:
#saída
    print('O número menor é {}'.format(numero3))