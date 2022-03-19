"""
Esse programa exibe a conversão de dólar para real nos
valores de 1 a 99 dólares
"""

real = float(input('digite o valor de um dólar em real: '))

for dolar in range(1,100):

 print ('US$ %.2f = R$ %.2f' % (dolar,dolar*real))
 
 print ('-' * 25)