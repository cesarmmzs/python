"""
Quanto ganha por hora
horas trabalhadas no mês

calcular salario total
imposto de renda 11%
inss 8%
5% sindicato
salario liquido
"""

salhora=float(input('Quanto você ganha por hora? '))
horasmes=int(input('Quantas horas inteiras você trabalha por mês?'))

salbruto=(salhora*horasmes)
IdR=(salbruto*0.11)
INSS=(salbruto*0.08)
sind=(salbruto*0.05)
descontos=(IdR+INSS+sind)
salliquido=(salbruto-descontos)

print('+ Salário Bruto : R${:.2f}'.format(salbruto))
print('- IR (11%) : R${:.2f}'.format(IdR))
print('- INSS (8%) : R${:.2f}'.format(INSS))
print('- Sindicato ( 5%) : R${:.2f}'.format(sind))
print('= Salário Liquido : R${:.2f}'.format(salliquido))
