sal_at=float (input('Por favor, informe seu salário: '))

if sal_at>0 and sal_at<=280:
    aum = sal_at*0.20
    sal_novo=aum+sal_at
    pct_aum=('20%')

elif sal_at>280 and sal_at<=700:
    aum = sal_at*0.15
    sal_novo = aum+sal_at
    pct_aum=('15%')

elif sal_at>700 and sal_at<=1500:
    aum= sal_at*0.10
    sal_novo= aum+sal_at
    pct_aum=('10%')

elif sal_at>1500:
    aum= sal_at*0.05
    sal_novo= aum+sal_at
    pct_aum=('5%')

print('Seu salário era: R${0:.2f}'.format(sal_at))
print('O percentual de aumento aplicado foi de: {0}'.format(pct_aum))
print('O valor do aumento foi de: R${0:.2f}'.format(aum))
print('Seu novo salário é: R${0:.2f}'.format(sal_novo))
