a=int(input('Дистанция первого дня: '))
b=int(input('Требуемая дистанция: '))
с=0.1
d=1

while a<=b:
    print (f'{d}-ый день: ',a)
    a = round(a * (1 + 0.1), 2)
    d=d+1
a = round(a, 2)
print (f'{d}-ый день: ',a)