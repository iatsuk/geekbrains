# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
#
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

mn = int(input('Введите нижнюю границу для целого числа: '))
mx = int(input('Введите верхнюю границу для целого числа: '))
print(random.randint(mn, mx))

mn = float(input('Введите нижнюю границу для вещественного числа: '))
mx = float(input('Введите верхнюю границу для вещественного числа: '))
print(random.uniform(mn, mx))

mn = ord(input('Введите нижнюю границу для символа: '))
mx = ord(input('Введите верхнюю границу для символа: '))
print(str(chr(random.randint(mn, mx))))
