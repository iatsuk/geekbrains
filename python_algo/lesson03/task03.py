# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

length = int(input('Введите длину массива:'))
array = [random.randint(0, 100) for _ in range(length)]
print(array)

minimal = array[0]
minimal_idx = 0
maximal = array[0]
maximal_idx = 0
for i in range(len(array)):
    if minimal > array[i]:
        minimal = array[i]
        minimal_idx = i
    if maximal < array[i]:
        maximal = array[i]
        maximal_idx = i
array[minimal_idx], array[maximal_idx] = array[maximal_idx], array[minimal_idx]
print(array)
