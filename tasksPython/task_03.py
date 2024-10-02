'''
Дан список элементов произвольной природы. Необходимо разработать метод
max_odd(array), который определит максимальный нечетный элемент (21.000 = 21 и
тоже считается нечетным элементом). Вернуть None, если таких элементов нет в
переданном массиве.

Тесты для примеров и проверки:
max_odd([1, 2, 3, 4, 4]) # => 3
max_odd([21.0, 2, 3, 4, 4]) # => 21
max_odd(['ololo', 2, 3, 4, [1, 2], None]) # => 3
max_odd(['ololo', 'fufufu']) # => None
max_odd([2, 2, 4]) # => None
'''
def max_odd(array):
    max_odd_value = None

    for item in array:
        # Проверяем, является ли элемент числом
        if isinstance(item, (int, float)):
            # Проверяем, нечетное ли число
            if item % 2 != 0:
                # Сравниваем с текущим максимальным нечетным значением
                if max_odd_value is None or item > max_odd_value:
                    max_odd_value = int(item)

    return max_odd_value

# Тесты
print(max_odd([1, 2, 3, 4, 4]))                
print(max_odd([21.0, 2, 3, 4, 4]))             
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))  
print(max_odd(['ololo', 'fufufu']))              
print(max_odd([2, 2, 4]))                        
