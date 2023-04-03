""" Faça um Programa que verifique se uma letra digitada é "F" ou "M".
 Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""
letra = input('Digite a letra: ').upper()
if letra == 'F':
    print('Femenino')
elif letra == 'M':
    print('Masculino')
else:
    print('Sexo invalido!')