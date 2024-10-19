first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Сборка списка длин строк из first_strings, длина которых не меньше 5 символов
first_result = [len(string) for string in first_strings if len(string) >= 5]

# Сборка списка пар слов одинаковой длины из двух списков
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Сборка словаря с парой ключ-значение, где ключ - строка, а значение - её длина
third_result = {string: len(string) for string in first_strings + second_strings if len(string) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)
