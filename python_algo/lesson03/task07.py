# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

length = int(input('Введите длину массива:'))
array = [random.randint(0, 10) for _ in range(length)]
print(array)

minimal1 = array[1]
minimal2 = array[0]
for i in range(2, len(array)):
    if minimal1 > array[i]:
        if minimal2 > minimal1:
            minimal2 = minimal1
        minimal1 = array[i]
        continue
    if minimal2 > array[i]:
        minimal2 = array[i]
print('Два наименьших элемента:', minimal1, minimal2)
