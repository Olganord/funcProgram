from random import choice


first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f:
            for index, data in enumerate(data_set, start=1):
                f.write(f"{index} {data}\n")

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        # Инициализация атрибута words с переданными строками
        self.words = words

    def __call__(self):
        # Используем функцию choice для случайного выбора слова из words
        return choice(self.words)


# Создаем экземпляр MysticBall с примерами слов
first_ball = MysticBall('Да', 'Нет', 'Наверное')


print(first_ball())
print(first_ball())
print(first_ball())
