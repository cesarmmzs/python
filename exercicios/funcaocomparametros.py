def soma(num1,num2):
    s = num1 + num2
    print(s)


soma(10,10)
soma(100,100)
soma(20,43)

def dobra(lst):
    for pos in range(len(lst)):
        lst[pos]*=2


salarios=[300,450,137,220,700]
print(salarios)
dobra(salarios)
print(salarios)