# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

s1 = ord(input('Введите первую букву(A-z): ').lower())
s2 = ord(input('Введите вторую букву(A-z): ').lower())
print(f'Позиция первой буквы: {s1 - ord("a") + 1}')
print(f'Позиция второй буквы: {s2 - ord("a") + 1}')
print(f'Количество букв между ними: {s2 - s1 - 1}')
