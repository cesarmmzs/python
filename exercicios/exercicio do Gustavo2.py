salhora=15

horasT=int(input('Informe quantas horas voce trabalhou esta semana: '))

if horasT<=40:
    salario = salhora * horasT
    print('O salário é {0:.2f}'.format(salario))

elif horasT>40:
    
    salario = salhora * horasT
    salarioextra = (horasT-40)*0.5+salario

    print('O salário é {0:.2f}'.format(salarioextra))