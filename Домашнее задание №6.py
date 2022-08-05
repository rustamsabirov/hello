# Домашнее задание №6
viru4ka=int(input('Введите выручку фирмы: '))
izderjka=int(input('Введите издержки фирмы: '))
renta=(viru4ka-izderjka)/viru4ka
if viru4ka>izderjka:
    print('Фирма в прибыли')
elif viru4ka==izderjka:
    print('Прибыль равна убыткам')
else:
    print('Фирма в прибыли')
renta=round((viru4ka-izderjka)/viru4ka,2)
print('Рентабельность: ',renta)
stat_firma=int(input('Введите численность сотрудников фирмы: '))
pfrs=(viru4ka-izderjka)/stat_firma
print('Прибыль фирмы в расчёте на одного сотрудника: ',pfrs)


