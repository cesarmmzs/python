salhr=float(input('Informe quanto você ganha por hora trabalhada: '))
hrmes=int(input('Quantas horas você trabalha por mês? '))

salbruto=salhr*hrmes

IR=salbruto*0.11 #imposto de renda 11%

INSS=salbruto*0.08 #inss 8%

sind=salbruto*0.05 #sindicato 5%

desc=IR+INSS+sind #total descontos

salliq=salbruto-desc #salario liquido
"""
resultados (utilizei o format para facilitar a resolução dos resultados, e ":.2f" para limitar as casas decimais)
"""

print('Salário Bruto: RS{0:.2f}'.format(salbruto))
print('')
print('DESCONTOS:')
print('Imposto de renda(11%): R${0:.2f}'.format(IR))
print('INSS(8%): R${0:.2f}'.format(INSS))
print('Sindicado(5%): R${0:.2f}'.format(sind))
print('')
print('Salário Líquido: R${0:.2f}'.format(salliq))