for x in range(5):

   print("ENTRADA DE DADOS DO ALUNO")
   matricula=int(input("Digite a matricula do aluno...: "))
   nota1=float(input("Digite a nota da avaliação 1..: "))
   nota2=float(input("Digite a nota da avaliação 2..: "))
   faltas=int(input("Digite a quantidade de faltas : "))

   media = (nota1 * 2 + nota2 * 3)/5
   pres = (float)(80-faltas) * 100 / 80

   print("LISTA DOS DADOS DO ALUNO")

   print("Média final..............:",media)
   print("Percentual de presença...:",pres)

   if media >= 6 and pres >= 75:
       print("Resultado final: Aprovado")
   elif media < 6 and pres >= 75:
       print("Resultado final: Reprovado por média")
   elif media >= 6 and pres < 75:
       print("Resultado final: Reprovado por falta")
   else:
       print("Resultado final: Reprovado por média e por falta")