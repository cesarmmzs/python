nota = 0
contnota = 0
notastring=''
soma=0
valacima=0
ab7=0

while (nota != -1): #definindo condição de loop com while
    nota=int(input('Digite a quantidade de notas desejada (O programa encerrará quando for inserido "-1"):')) #recebe valor da nota
    
    if nota == (-1): #condição if criada dentro do loop
        print('-'*50)
        print('FIM DO PROGRAMA')
        print('-'*50)
        print('Foram lidas {0} notas.'.format(contnota))
        print('Os dados inseridos foram: {0}'.format(notastring))
        print('De trás para frente, os dados inseridos foram:')
        for revertido in (notastring[::-1]): print(revertido) #usando o for para escrever na linha abaixo, sempre que 'revertido' tiver valor para receber de 'notastring'
        print('A soma das notas é {0}'.format(soma))
        print('A média das notas é {0}'.format(media))
        print('{0} valores estão acima da média.'.format(valacima))
        print('{0} valores estão abaixo de 7.'.format(ab7))
        break   #fim do loop caso a condição do if seja cumprida

    else:   #caso não seja:
        notastring=(notastring+' '+str(nota)) #acumula os valores inseridos numa variável string
        soma=nota+soma      #acumulando a soma do valor enquanto o loop estiver ativo
        contnota+=1     #recebendo a quantidade de notas enquanto o loop estiver ativo
        media=soma/contnota     #definindo a média enquanto o loop estiver ativo
        revertido = (notastring[::-1])    #recebendo os valores da variável 'notastring' dá última posição para a primeira

        if (nota>media):        #uma condição dentro da condição anterior
            valacima+=1         #caso a condição seja cumprida, atribui +1 à quantidade de números acima da média
            
        if (nota<7):            #além da condição acima, recebe mais uma condição para atribuir +1 aos números menores que 7   
            ab7 += 1