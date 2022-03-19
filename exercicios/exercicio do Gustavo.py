n=str(input('Informe seu nome: '))
tipo=str(input('Informe o tipo do apartamento?(A,B,C ou D)'))
diaria=int(input('Informe a quantidade de diárias: '))
cons=float(input('Informe a quantia gasta no consumo interno: '))

if tipo=='A':
    valorD=400
elif tipo=='B':
    valorD=300
elif tipo=='C':
    valorD=200
elif tipo=='D':
    valorD=100

totdiaria=valorD*diaria
subtot=totdiaria+cons
taxa=subtot*0.10
total=taxa+subtot

print('O nome do hóspede é {0} e o tipo de apartamento {1} as diárias {2} e o consumo interno {3:.2f}'.format(n,tipo,diaria,cons))
print('O subtotal é: {0}'.format(subtot))
print('O valor da taxa de serviço é: {0:.2f}'.format(taxa))
print('O total é: {0}'.format(total)) 