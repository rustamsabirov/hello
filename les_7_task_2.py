"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random

def my_sort(array):
    if len(array) <= 1:
        return array

    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    left = my_sort(array[:len(array) // 2])
    right = my_sort(array[len(array) // 2:])
    i, j = 0, 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        array[i + j] = left[i]
        i += 1
    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array

data = [round(random.uniform(1, 50, ), 1) for i in range(10)]
print(f'Исходный массив: {data}')

my_sort(data)
print(f'Массив по возрастанию: {data}')

