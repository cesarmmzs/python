valor=[]
contloop=soma=media=cont_val_acima=cont_val_ab7=0

while contloop!=1:
    valor.append(int(input('Digite a quantidade de notas desejada (O programa encerrará quando for inserido "-1"):')))
    contloop = valor.count(-1)
    soma=soma+valor[-1]

else:
    soma=soma-valor[-1]
    valor.pop()
    valor2=valor[:]

    print('-'*50)
    print('FIM DO PROGRAMA')
    print('-'*50)
    print('Foram lidas {0} notas.'.format(len(valor))) 
    print('Os dados inseridos foram: {0}'.format(valor)) 
    print('De trás para frente, os dados inseridos foram:')
    for dados in reversed(valor):
        print(dados)                                        
    print('A soma dos valores é: {0}'.format(soma))

    media=soma/len(valor)
    print('A média das notas é {0:.2f}'.format(media))

    for dados in range(len(valor)):
        teste = valor.pop(-1)
        if teste>media:
            cont_val_acima+=1
    print('{0} valores são maiores que a média'.format(cont_val_acima))

    for dados in range(len(valor2)):
        teste = valor2.pop(-1)
        if teste<7:
            cont_val_ab7+=1
    print('{0} valores são menores que 7'.format(cont_val_ab7))
    print('-'*50)
    