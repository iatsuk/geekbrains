# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
import random


def order_statistics(array, k):
    def partition(array, left, right):
        idx = left + int((right - left) / 2)
        mid = array[idx]
        lower = []
        middle = []
        higher = []
        for i in range(left, right):
            if array[i] < mid:
                lower.append(array[i])
            elif array[i] > mid:
                higher.append(array[i])
            else:
                middle.append(array[i])
        ordered = lower + middle + higher
        for i in range(left, right):
            array[i] = ordered[i - left]
        return left + len(lower)

    left = 0
    right = len(array)
    while True:
        mid = partition(array, left, right)
        if mid == k:
            return array[mid]
        elif k < mid:
            right = mid
        else:
            left = mid + 1


if __name__ == '__main__':
    # создаем массив и заполняем случайными числами
    m = 5 * 2 + 1
    a = [random.randint(-100, 100) for _ in range(m)]
    print(a)
    # находим медиану
    med_idx = int(m / 2) - 1
    med = order_statistics(a, med_idx)
    print('Медиана:', med)
    # проверка решения
    a.sort()
    print('Решение', 'верное' if a[med_idx] == med else 'не верное')
