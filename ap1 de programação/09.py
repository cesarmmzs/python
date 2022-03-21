salarios=[[200,299],[300,399],[400,499],[500,599],[600,699],[700,799],[800,899],[900,999],[1000,99999]]
armsalario=[]
contloop=0
cont200=0
cont300=0
cont400=0
cont500=0
cont600=0
cont700=0
cont800=0
cont900=0
cont1000=0

while contloop!=(-1):
    vendas=float(input('Informe o valor das vendas brutas(Caso o valor seja 0, o programa termina.): R$'))
    salario=200+(vendas*0.09)
    armsalario.append(salario)
    print('Existem {0} índices em "vendas"'.format(len(salarios)))
    print('Existem {0} índices em "armsalário"'.format(len(armsalario)))

    if vendas == (0):
        for armsalario[:] in salarios[0[:]]:
            cont200+=1
        for armsalario[:] in salarios[1[:]]:
            cont300+=1
        for armsalario[:] in salarios[2[:]]:
            cont400+=1
        for armsalario[:] in salarios[3[:]]:
            cont500+=1
        for armsalario[:] in salarios[4[:]]:
            cont600+=1
        for armsalario[:] in salarios[5[:]]:
            cont700+=1
        for armsalario[:] in salarios[6[:]]:
            cont800+=1
        for armsalario[:] in salarios[7[:]]:
            cont900+=1
        for armsalario[:] in salarios[8[:]]:
            cont1000+=1
        break