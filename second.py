
money=input("Введите сумму:")
m=int(money)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
I=list(per_cent.values())
M=[x*m/100 for x in I]
print(M)
print("Максимальная сумма, которую вы можете заработать —",max(M))
