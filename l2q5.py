"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
    ◦ A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    ◦ A mensagem "Reprovado", se a média for menor do que sete;
    ◦ A mensagem "Aprovado com Distinção", se a média for igual a dez."""

nota = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota + nota2)/2

print('media', media)

if media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
else:
    print('Aprovado com Distinção')