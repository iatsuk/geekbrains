# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")  # p a pa ap pap apa
# 6
# func("sova")  # s o v a so ov va sov ova
# 9
import hashlib


def func(s):
    def extract_substrings(s):
        result = set()
        for i in range(1, len(s) + 1):
            for j in range(len(s) - i + 1):
                new_substring = s[j:j + i]
                new_hash = hashlib.sha1(new_substring.encode("utf-8")).hexdigest()
                if new_hash not in result:
                    result.add(new_hash)
        return result

    hash_set = set()
    strings = [x for x in s.split(' ') if x.strip()]
    for string_without_spaces in strings:
        hash_set = hash_set.union(extract_substrings(string_without_spaces))
    if len(strings) == 1:
        return len(hash_set) - 1
    else:
        return len(hash_set)


print(func("papa"))
print(func(" pa  papa r"))
print(func("sova"))
