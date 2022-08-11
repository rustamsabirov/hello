def my_sum(*args):
    summa = 0
    vixod = False
    for number in args:
        try:
            if number:
                summa += float(number)
        except ValueError:
            vixod = True
    return summa, vixod

total_summa = 0

while True:
    numbers_string = input('Введите числа через пробел: ').split(' ')
    summa, stop = my_sum(*numbers_string)
    total_summa += summa
    print(f'сумма {total_summa}')

    if stop:
        break
