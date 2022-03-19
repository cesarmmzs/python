"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez
"""

n1=float(input('Insira sua primeira nota: '))
n2=float(input('Insira sua segunda nota: '))

media=(n1+n2)/2

while n1 > -1 and n2 > -1:
    if media>10:
        print('Dados Inválidos, por favor tente novamente com dados válidos.')
        break    

    if media==10:
        print('Aprovado com Distinção')
        break

    elif media>=7:
        print('Aprovado')
        break

    elif media<7:
        print('Reprovado')
        break

if media<7:
    print('Dados Inválidos, por favor tente novamente com dados válidos.')