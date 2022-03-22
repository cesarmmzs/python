salarios=[]
cont_intervalos=[0]*9
def msg(ind,val1,val2):
    print('{0} vendedores receberam salário entre R${1} e R${2}'.format(cont_intervalos[ind],val1,val2))


while True:
    vendasB=float(input('Informe o valor de vendas brutas: R$'))
    salarios.append(float(vendasB*0.09)+200)
    res=str(input('Inserir outro valor?[S/N]'))

    if res in 'Nn':
        break

for cada_salario in salarios:
    ind = int((cada_salario-200)/100)
    ind_max=len(cont_intervalos)-1
    ind = min(ind,ind_max)
    cont_intervalos[ind]+=1
    
msg(0,200,299)
msg(1,300,499)
msg(2,400,499)
msg(3,500,599)
msg(4,600,699)
msg(5,700,799)
msg(6,800,899)
msg(7,900,999)
print(f'{cont_intervalos[8]} vendedores receberam salário acima de R$1000')