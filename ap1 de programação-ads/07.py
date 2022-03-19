num=int(input('Informe um número inteiro de 1 a 10: '))
cont=0

print('-'*25)
print('TABUADA DE {0}:'.format(num))

while cont<10:
    cont+=1
    res=(num*cont)
    print('{0}X{1}={2}'.format(num,cont,res))
