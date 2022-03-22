salarios=[]
cont_intervalos=[0]*9
while True:
    vendasB=float(input('Informe o valor de vendas brutas: R$'))
    salarios.append(float(vendasB*0.09)+200)
    res=str(input('Inserir outro valor?[S/N]'))

    if res in 'Nn':
        break

for salario in salarios:
    ind = int((salario-200)/100)
    ind_max=len(cont_intervalos)-1
    ind = min(ind,ind_max)
    cont_intervalos[ind]+=1
    
print(f'{cont_intervalos[0]} vendedores receberam salário entre R$200 e R$299')
print(f'{cont_intervalos[1]} vendedores receberam salário entre R$300 e R$299')
print(f'{cont_intervalos[2]} vendedores receberam salário entre R$400 e R$299')
print(f'{cont_intervalos[3]} vendedores receberam salário entre R$500 e R$299')
print(f'{cont_intervalos[4]} vendedores receberam salário entre R$600 e R$299')
print(f'{cont_intervalos[5]} vendedores receberam salário entre R$700 e R$299')
print(f'{cont_intervalos[6]} vendedores receberam salário entre R$800 e R$299')
print(f'{cont_intervalos[7]} vendedores receberam salário entre R$900 e R$299')
print(f'{cont_intervalos[8]} vendedores receberam salário acima de R$1000')