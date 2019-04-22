# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите величину ряда: '))
elem = 1.0
series_sum = 0.0
for _ in range(n):
    series_sum += elem
    elem = elem / -2
print(series_sum)
