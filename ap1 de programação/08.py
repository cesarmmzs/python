nota = 0
contnota = 0
notastring=''
soma=0
valacima=0
ab7=0

while (nota != -1): #definindo condição de loop
    nota=int(input('Digite a quantidade de notas desejada (O programa encerrará quando for inserido "-1"):')) #recebe valor da nota
    
    if nota == (-1): #condição criada dentro do loop
        print('-'*30)
        print('Foram lidas {0} notas.'.format(contnota))
        print('Os dados inseridos foram: {0}'.format(notastring))
        print('De trás para frente, os dados inseridos foram:')
        for revertido in (notastring[::-1]): print(revertido)
        print('A soma das notas é {0}'.format(soma))
        print('A média das notas é {0}'.format(media))
        print('{0} valores estão acima da média.'.format(valacima))
        print('{0} valores estão abaixo de 7.'.format(ab7))
        print('Fim da contagem dos valores.')
        break   #fim do loop caso a condição seja cumprida

    else:   #caso não seja:
        notastring=(notastring+' '+str(nota)) #acumula valores inseridos numa variável string
        soma=nota+soma      #acumulando a soma do valor enquanto o loop estiver ativo
        contnota+=1     #recebendo a quantidade de notas enquanto o loop estiver ativo
        media=soma/contnota     #definindo a média enquanto o loop estiver ativo
        revertido = (notastring[::-1])

        if (nota>media):        #uma condição dentro da condição anterior
            valacima+=1         #caso a condição seja cumprida, atribui +1 à quantidade de números acima da média
            print('-'*30)
            print('Foram lidas {0} notas.'.format(contnota))
            print('Os dados inseridos foram: {0}'.format(notastring))
            print('De trás para frente, os dados inseridos foram:')
            for revertido in (notastring[::-1]): print(revertido)
            print('A soma das notas é {0}'.format(soma))
            print('A média das notas é {0}'.format(media))
            print('{0} valores estão acima da média.'.format(valacima))
            print('{0} valores estão abaixo de 7.'.format(ab7))
            

        if (nota<7):            #além da condição acima, recebe mais uma condição para atribuir mais um valor à outra variável   
            ab7 += 1
            print('-'*30)
            print('Foram lidas {0} notas.'.format(contnota))
            print('Os dados inseridos foram: {0}'.format(notastring))
            print('De trás para frente, os dados inseridos foram:')
            for revertido in (notastring[::-1]): print(revertido)
            print('A soma das notas é {0}'.format(soma))
            print('A média das notas é {0}'.format(media))
            print('{0} valores estão acima da média.'.format(valacima))
            print('{0} valores estão abaixo de 7.'.format(ab7))
                
        else:                   #caso nenhuma das duas condições sejam cumpridas, os variáveis referentes no código deixam de receber seus respectivos acúmulos
            print('-'*30)
            print('Foram lidas {0} notas.'.format(contnota))
            print('Os dados inseridos foram: {0}'.format(notastring))
            print('De trás para frente, os dados inseridos foram:')
            for revertido in (notastring[::-1]): print(revertido)
            print('A soma das notas é {0}'.format(soma))
            print('A média das notas é {0}'.format(media))
            print('{0} valores estão acima da média.'.format(valacima))
            print('{0} valores estão abaixo de 7.'.format(ab7))