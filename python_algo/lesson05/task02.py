# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Не использовать функции hex() и/или int().

from collections import deque

hex_words = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def hex2dec(num):
    return sum([hex_words.index(v) * 16 ** idx for idx, v in enumerate(num)])


def dec2hex(num):
    result = deque()
    while num != 0:
        result.appendleft(hex_words[num % 16])
        num = num // 16
    return result


# ввод данных
a16 = deque(input('Введите первое число: ').upper())
b16 = deque(input('Введите второе число: ').upper())

# переводим в десятичную систему исчисления
a16.reverse()
b16.reverse()
a10 = hex2dec(a16)
b10 = hex2dec(b16)

# производим математические операции
ab_sum10 = a10 + b10
ab_prod10 = a10 * b10

# переводим в шестнадцатиричную систему исчисления
print('Сумма: ', dec2hex(ab_sum10))
print('Произведение: ', dec2hex(ab_prod10))
