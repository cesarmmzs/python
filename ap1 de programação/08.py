valor=[50]
x=0
soma=0
media=0

val_acima=[]
val_ab7=[]
cont_val_acima=0
cont_val_ab7=0

while x!=1:
    valor.append(int(input('Digite a quantidade de notas desejada (O programa encerrará quando for inserido "-1"):')))
    x = valor.count(-1) 
    soma=soma+valor[-1]

    if valor[-1]<7:
        cont_val_ab7+=1

        if -1 in valor:
            soma=soma-valor[-1]
            del valor[0]
            valor.pop()
            cont_val_ab7-=1

            print('-'*50)
            print('FIM DO PROGRAMA')
            print('-'*50)
            print(f'Foram lidas {len(valor)} notas.')
            print('Os dados inseridos foram: {0}'.format(valor))
            print('De trás para frente, os dados inseridos foram:')
            for i in reversed(valor):
                print(i)
            print('A soma dos valores é: {0}'.format(soma))
            media=soma/len(valor)
            print('A média das notas é {0:.2f}'.format(media))
            print('{0} valores são menores que 7'.format(cont_val_ab7))

            for i in range(len(valor)):
                teste = valor.pop(-1)
                if teste>media:
                    cont_val_acima+=1
            print('{0} valores são maiores que a média'.format(cont_val_acima))
            print('-'*50)