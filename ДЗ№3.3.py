def my_func(a,b,c):
    return print(f'Сумма двух наибольших аргументов = {a + b + c - min(a, b, c)}')

my_func(
    int(input('Аргумент №1: ')),
    int(input('Аргумент №2: ')),
    int(input('Аргумент №3: '))
)