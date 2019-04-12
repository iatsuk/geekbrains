# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
from functools import reduce

n = input('Введите трехзначное число: ')
nums = list(map(int, n))
print('Сумма:', sum(nums))
print('Произведение:', reduce(lambda x, y: x * y, nums, 1))
