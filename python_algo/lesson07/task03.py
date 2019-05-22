# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
import random
from collections import defaultdict


def order_statistics(array, k):
    def partition(array):
        pivot = array[len(array) // 2]
        data = defaultdict(list)
        for e in array:
            if e < pivot:
                data['lower'].append(e)
            elif e > pivot:
                data['higher'].append(e)
            else:
                data['same'].append(e)
        return data['lower'], data['same'], data['higher']

    while True:
        lower, same, higher = partition(array)
        if (k >= len(lower)) and (k < len(lower) + len(same)):
            return same[0]
        elif k < len(lower):
            array = lower
        else:
            k = k - len(lower) - len(same)
            array = higher


if __name__ == '__main__':
    # создаем массив и заполняем случайными числами
    m = 5 * 2 + 1
    a = [random.randint(-100, 100) for _ in range(m)]
    print(a)
    # находим медиану
    med_idx = m // 2
    med = order_statistics(a, med_idx)
    print('Медиана:', med)
    # проверка решения
    a.sort()
    print('Решение', 'верное' if a[med_idx] == med else 'не верное')
