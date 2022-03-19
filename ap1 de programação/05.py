n1=float(input('Insira sua primeira nota: '))
n2=float(input('Insira sua segunda nota: '))

media=(n1+n2)/2

if media==10:
    print('Aprovado com distinção')

elif media>=7:
    print('Aprovado')

elif media<7:
    print('Reprovado')