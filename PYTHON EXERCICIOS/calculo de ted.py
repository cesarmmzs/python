"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
import math

p_arqMB=float(input('Informe o nome do arquivo(MB): '))
vel_link=int(input('Informe a velocidade do link de internet(Mbps): '))

p_arqMb=(p_arqMB*8)
print(p_arqMb,'Mb')

ted= math.ceil((p_arqMb/vel_link)/60)

print('A estimativa de tempo de espera do download é de {0} minutos'.format(ted))