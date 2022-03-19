#importa o módulo math, que é usado para funçoes matemáticas
import math

#recebendo o valor da área
areapp=float(input('Informe o tamanho da área a ser pintada(m²): '))

#calculo p saber quanto de tinta usar em Litros
cobtinta=float(areapp/6)

#litros e preço por produto
ltam=(18)
lpreco=(80.00)
gtam=(3.6)
gpreco=(25.00)

#1a situação
qtlat=math.ceil(cobtinta/ltam)
precolat=(qtlat*lpreco)

#2a situação
qtgal=math.ceil(cobtinta/gtam)
precogal=(qtgal*gpreco)

#3a situação
"""
aqui o precisamos saber quantas latas comprar até sobrar menos de 18 litros, pela diferença "%"
depois dividir pela quantidade de litros do galão
multiplicar o resultado pelo preço do galão e obter a quantia a ser gasta com galão
"""
qtgals=math.ceil((cobtinta%ltam)/gtam)
precogals=qtgals*gpreco
"""
para saber quantas latas serão necessárias até que falta menos que 18 litros, deverá ser feita a divisão de inteiros "//"
e o preço por essas latas multiplicando o resultado dessa divisão pelo preço da lata
"""
qtlats=(cobtinta//ltam)
precolats=(qtlats*lpreco)
"""
depois só precisamos somar o preço das latas utilizadas com o preço dos galões utilizados
"""
precocombinacao = precolats+precogals
#informa a quantidade de tinta a ser gasta
print('Você gastará {:.2f}L de tinta, portanto:'.format(cobtinta))

#informa a quantidade dos produtos a ser usada e seus respectivos preços
print('Caso queira comprar apenas latas(18L), deverá comprar {0:.2f} por R${1:.2f}'.format(qtlat,precolat))
print('Caso queira comprar apenas galões(3,6L), deverá comprar {0:.2f} por R${1:.2f}'.format(qtgal,precogal))
print(
    'Caso queira comprar alternadamente para que haja menos desperdício, deverá comprar {0:.2f} latas por R${1:.2f} e {2:.2f} galões por R${3:.2f}'.format(
        qtlats,precolats,qtgals,precogals
        )
    )