def is_prime(func):

    def wrapper(*args, **kwargs):
        result_ = func(*args, **kwargs)  # Получаем результат функции sum_three
        if result_ < 2:
            print("Составное")  # 0 и 1 не являются простыми числами
            return result

        for i in range(2, int(result_**0.5) + 1):
            if result_ % i == 0:
                print("Составное")  # Находим делитель, значит число составное
                return result_
        print("Простое")  # Если делителей не нашли, число простое
        return result_

    return wrapper


@is_prime  # Применяем декоратор к функции sum_three
def sum_three(a, b, c):
    return a + b + c  # Складываем три числа


# Пример использования
result = sum_three(2, 3, 6)  # Вызов функции

print(result)  # Выводим результат

"""В этом коде определены две функции. Первая, sum_three, складывает три числа, 
а вторая, декоратор is_prime, проверяет, простое ли это число. Если число простое, 
печатается "Простое"; если составное — "Составное"."""