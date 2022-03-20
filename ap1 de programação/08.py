valor=[]
valacima=[]
ab7=[]
contvalacima=0
contvalab7=0
x=0
soma=0
media=0

while x!=1:
    valor.append(input('Digite a quantidade de notas desejada (O programa encerrará quando for inserido "-1"):'))
    x = valor.count('-1')
    soma=(soma+int(valor[-1]))
    if '-1' in valor:
        soma=(soma-int(valor[-1]))
        media=soma/len(valor)
        del valor[-1]

        contvalacima=valacima.count(all>media)
        contvalab7=ab7.count(all<7)
        
        print('-'*50)
        print('FIM DO PROGRAMA')
        print('-'*50)
        print(f'Foram lidas {len(valor)} notas.')
        print('Os dados inseridos foram: {0}'.format(valor))
        print('De trás para frente, os dados inseridos foram:')
        for i in reversed(valor):
            print(i)
        print('A soma dos valores é: {0}'.format(soma))
        print('A média das notas é {0}'.format(media))
        print('{0:.2f} valores estão acima da média.'.format(contvalacima))
        print('{0} valores estão abaixo de 7.'.format(contvalab7))
        break
