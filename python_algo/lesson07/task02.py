# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge_sort(array):
    if len(array) <= 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    else:
        left = merge_sort(array[:len(array) // 2])
        right = merge_sort(array[len(array) // 2:])
        result = []
        li, ri = 0, 0
        while li < len(left) or ri < len(right):
            if (li < len(left)) and ((ri < len(right) and left[li] < right[ri]) or (ri >= len(right))):
                result.append(left[li])
                li += 1
            else:
                result.append(right[ri])
                ri += 1
        return result


if __name__ == '__main__':
    size = 10
    # генерируем
    a = [random.randrange(0, 50) for _ in range(size)]
    print(a)
    # сортируем
    b = merge_sort(a)
    print(b)
    # проверяем
    a.sort()
    print('верно' if a == b else 'не верно')
