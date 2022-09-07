"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import defaultdict
from collections import deque

def my_str(string):
    s = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        s += table[num[i]] * 16 ** i
    return s

def my_hex(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)

my_tab = '0123456789ABCDEF'
table = defaultdict(int)
i = 0
for key in my_tab:
    table[key] += i
    i += 1

num_1 = my_str(input('Введите первое число в шестнадцатиричном формате: ').upper())
num_2 = my_str(input('Введите второе число в шестнадцатиричном формате: ').upper())
print(f'Сумма чисел: {my_hex(num_1 + num_2)}')
print(f'Произведение чисел: {my_hex(num_1 * num_2)}')