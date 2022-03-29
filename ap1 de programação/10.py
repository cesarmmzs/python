def valorPagamento(a,b):
    global val_pagar
    val_pagar=float(a)
    if b>0:
        val_pagar=(val_pagar+(a*0.03))+(b*0.001)
    

def msgfim():
    print('-=-'*10)
    print('      FIM DO PROGRAMA \n CONFIRA O RELATÓRIO ABAIXO:')
    print('-=-'*10)


cont_prest=[]
val_pagar=soma_prest=0

while True:
    val_prest=float(input('Informe o valor da prestação: R$'))
    if val_prest==0:
        break
    dias_at=int(input('Informe o número de dias de atraso da prestação: '))
    valorPagamento(val_prest,dias_at)
    soma_prest=soma_prest+val_pagar
    cont_prest.append(val_pagar)
    print(f'O valor a ser pago é {val_pagar}')

msgfim()
print(f'Foram pagas {len(cont_prest)} prestações no dia')
print(f'O valor prestações no dia é de RS{soma_prest:.2f}\n')