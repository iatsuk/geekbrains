# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5, если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

length = int(input('Введите длину массива:'))
array = [random.randint(0, 100) for _ in range(length)]
print(array)

array2 = [i for i in range(len(array)) if array[i] % 2 == 0]
print(array2)

# or

array2 = [i for (i, v) in enumerate(array) if v % 2 == 0]
print(array2)
