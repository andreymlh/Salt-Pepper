'''
Дан список целых чисел. Необходимо разработать метод sort_list(list),который
поменяет местами все минимальные и максимальные элементы массива, а также
добавит в конец массива одно минимальное значение из него.

Тесты для примеров и проверки:
sort_list([]) # => []
sort_list([2, 4, 6, 8]) # => [8, 4, 6, 2, 2]
sort_list([1]) # => [1, 1]
sort_list([1, 2, 1, 3]) # => [3, 2, 3, 1, 1]
'''

def sort_list(lst):
    # Проверка на пустой список
    if not lst:  
        return []
    
    min_value = min(lst)
    max_value = max(lst)

    # Меняем местами все минимальные и максимальные элементы
    new_lst = [max_value if x == min_value else min_value if x == max_value else x for x in lst]

    # Добавляем одно минимальное значение в конец списка
    new_lst.append(min_value)

    return new_lst

# Тесты
print(sort_list([]))               
print(sort_list([2, 4, 6, 8]))     
print(sort_list([1]))               
print(sort_list([1, 2, 1, 3]))     
