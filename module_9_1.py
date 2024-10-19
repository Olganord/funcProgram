def apply_all_func(int_list, *functions):
    results = {}  # Создаем пустой словарь для хранения результатов
    for func in functions:
        try:
            # Применяем функцию к списку и сохраняем результат в словаре
            results[func.__name__] = func(int_list)
        except Exception as e:
            # В случае ошибки добавляем сообщение об ошибке
            results[func.__name__] = str(e)
    return results  # Возвращаем словарь с результатами


# Примеры вызова функции
print(apply_all_func([6, 20, 15, 9], max, min))  # {'max': 20, 'min': 6}
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))  # {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
print(apply_all_func([6, 20, 15, 9], round))
print(apply_all_func([6, "20", 15, 9], max))
