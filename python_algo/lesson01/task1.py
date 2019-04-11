# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
from functools import reduce

n = input('Введите трехзначное число: ')
vals = list(map(int, n))
print(f'Сумма: {sum(vals)}')
print(f'Произведение: {reduce(lambda x, y: x * y, vals, 1)}')
