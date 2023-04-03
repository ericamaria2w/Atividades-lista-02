"""11.As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
    ◦ Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    ◦ salários até R$ 280,00 (incluindo) : aumento de 20%
    ◦ salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    ◦ salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    ◦ salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    ◦ o salário antes do reajuste;
    ◦ o percentual de aumento aplicado;
    ◦ o valor do aumento;
    ◦ o novo salário, após o aumento."""
import math
 
salario = float(input('Digite seu salario: '))

if salario <= 280:
    aumento20 = salario +  ((20/100) * salario )
elif salario >= 290:
    aumento_15 = salario + ((15/100) * salario )
elif salario >= 700:
    aumento10 = salario + ((10/100) * salario)
elif salario >= 1500:
    aumento5 = salario + ((5/100) * salario)

print('Antes do reajuste: ', salario)

if salario == aumento20:
    print('O valor do seu salario agora é: ',aumento20)
elif salario == aumento_15:
    print('O valor do seu salario agora é: ',aumento_15)
elif salario == aumento10:
    print('O valor do seu salario agora é: ',aumento10)
else:
    print('O valor do seu salario agora é: ',aumento5)