'''
Дан список list и числовой диапазон range. Разработайте метод coincidence(list,
range) для определения элементов из массива list, значения которого входят в
указанный диапазон range. Если не передан хотя бы один из параметров, то
должен вернуться пустой массив.

Тесты для примеров и проверки:
coincidence([1, 2, 3, 4, 5], range(3, 6)) # => [3, 4, 5]
coincidence() # => []
coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)) # => [1, 2, 2.5]
'''


def coincidence(lst=None, rng=None):
    # Проверяем, переданы ли оба аргумента
    if lst is None or rng is None:
        return []

    # Инициализируем список для хранения совпадений
    result = []
    
    # Перебираем элементы списка
    for elem in lst:
        # Проверяем, является ли элемент числом и находится ли он в диапазоне
        if isinstance(elem, (int, float)) and elem >= rng.start and elem < rng.stop:
            result.append(elem)
    
    return result

# Тесты
print(coincidence([1, 2, 3, 4, 5], range(3, 6)))  
print(coincidence())                               
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))  


