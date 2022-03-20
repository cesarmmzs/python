val = 0
contval = 0
valstring=''
soma=0
valacima=0
ab7=0

while (val != -1): #definindo condição de loop com while
    val=int(input('Digite a quantidade de notas desejada (O programa encerrará quando for inserido "-1"):')) #recebe valor
    
    if val == (-1): #condição if criada dentro do loop
        print('-'*50)
        print('FIM DO PROGRAMA')
        print('-'*50)
        print('Foram lidas {0} notas.'.format(contval))
        print('Os dados inseridos foram: {0}'.format(valstring))
        print('De trás para frente, os dados inseridos foram:')
        for revertido in (valstring[::-1]): print(revertido) #usando o for para escrever na linha abaixo, sempre que 'revertido' tiver valor para receber de 'notastring'
        print('A soma das notas é {0}'.format(soma))
        print('A média das notas é {0}'.format(media))
        print('{0} valores estão acima da média.'.format(valacima))
        print('{0} valores estão abaixo de 7.'.format(ab7))
        break   #fim do loop caso a condição do if seja cumprida

    else:   #caso não seja:
        soma=val+soma      #acumulando a soma do valor enquanto o loop estiver ativo
        contval+=1     #recebendo a quantidade de valores enquanto o loop estiver ativo
        media=soma/contval     #definindo a média enquanto o loop estiver ativo
        revertido =(valstring[::-1])    #recebendo os valores da variável 'valstring' dá última posição para a primeira

        if (val>media):        #uma condição dentro da condição anterior
            valacima+=1         #caso a condição seja cumprida, atribui +1 à quantidade de números acima da média
            
        if (val<7):            #além da condição acima, recebe mais uma condição para atribuir +1 aos números menores que 7   
            ab7 += 1