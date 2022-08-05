# Домашнее задание №2
time=int(input('Введите время в секундах: '))
if time>3600:
    chas=time//3600
else:
    chas=0
time-=chas*3600

if time>60:
    minuta=time//60
else:
    minuta=0
time-=minuta*60

print('Время в формате чч:мм:сс {}:{}:{}'.format(chas,minuta,time))

# f'{chas}:{minuta}:{time}'