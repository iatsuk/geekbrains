# 4. Определить, какое число в массиве встречается чаще всего.

import random

length = int(input('Введите длину массива:'))
array = [random.randint(0, 10) for _ in range(length)]
print(array)

index = {}
most_often = 0
most_often_value = 0
for e in array:
    index[e] = index.get(e, 0) + 1
    if index[e] > most_often:
        most_often = index[e]
        most_often_value = e

print('Самое частое число:', most_often_value)
