# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

length = int(input('Введите длину массива:'))
array = [random.randint(0, 10) for _ in range(length)]
print(array)

minimal = array[0]
minimal_idx = 0
maximal = array[0]
maximal_idx = 0
for i in range(len(array)):
    if minimal >= array[i]:
        minimal = array[i]
        minimal_idx = i
    if maximal < array[i]:
        maximal = array[i]
        maximal_idx = i

if minimal_idx > maximal_idx:
    minimal_idx, maximal_idx = maximal_idx, minimal_idx
s = 0
for i in range(minimal_idx + 1, maximal_idx):
    s += array[i]
print('Сумма элементов между минимальным и максимальным', s)
