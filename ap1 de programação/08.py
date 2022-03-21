#'declarando' variáveis
valor=[]           #array que armazenará valores inseridos
contloop=0          #contador que definirá a quantidade de loops
soma=0              #armazena o valor da soma
media=0             #armazena a média
cont_val_acima=0    #armazena quantidade de números maiores que a média
cont_val_ab7=0      #armazena quantidade de números menores que 7

#Início do loop
while contloop!=1: #mantém o loop enquanto contloop for diferente de 1 (definido como '0')
    valor.append(int(input('Digite a quantidade de notas desejada (O programa encerrará quando for inserido "-1"):'))) #insere +1 dado em 'valor'
    contloop = valor.count(-1) #caso haja algum valor '-1' em valor, retorna 1
    soma=soma+valor[-1]  #recebe o ultimo valor inserido mais a soma do ultimo loop

    #Calcula e informa os dados pedidos
    if -1 in valor: #caso -1 tenha sido inserido:
        soma=soma-valor[-1] #subtrai a soma pelo ultimo valor inserido
        valor.pop() #remove o último índice
        valor2=valor[:] #copia o conteudo do array 'valor' para 'valor2'

        print('-'*50)
        print('FIM DO PROGRAMA') #anuncia o fim do programa
        print('-'*50)
        print('Foram lidas {0} notas.'.format(len(valor))) #diz quantos valores foram inseridos com base na quantidade de índices em 'valor'
        print('Os dados inseridos foram: {0}'.format(valor)) #mostra os valores da lista
        print('De trás para frente, os dados inseridos foram:')
        for dados in reversed(valor):
            print(dados)                                        #mostra os valores em ordem invertida, um acima do outro
        print('A soma dos valores é: {0}'.format(soma))         #mostra a soma

        #calculando a média
        media=soma/len(valor)                                   #calcula a média só depois do loop terminar
        print('A média das notas é {0:.2f}'.format(media))      #mostra a media

        #Recebendo valores maiores que a média
        for dados in range(len(valor)):
            teste = valor.pop(-1)
            if teste>media:                 #utiliza o for para realizar um loop definido pela quantidade de índices em valor
                cont_val_acima+=1           #a cada loop a variável 'teste' recebe o índice de 'valor' e o remove da lista, assim, limitando o loop. o código executado verifica se 'teste' é maior que a média e se sim, adiciona +1 ao respectivo contador.
        print('{0} valores são maiores que a média'.format(cont_val_acima)) #mostra os valores

        #Recebendo valores menores que 7
        for dados in range(len(valor2)):
            teste = valor2.pop(-1)
            if teste<7:   #faz basicamente o mesmo que o código acima, mas utilizando 'valor2', a cópia de valor, uma vez que o loop acima apaga o conteúdo da lista
                cont_val_ab7+=1
        print('{0} valores são menores que 7'.format(cont_val_ab7)) #mostra os valores
        print('-'*50)
        break