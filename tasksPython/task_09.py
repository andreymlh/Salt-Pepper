'''
Необходимо разработать метод connect_dicts(dict1, dict2), который соединит два
переданных словаря, значениями ключей в которых являются числа, и вернет
новый словарь, полученный по следующим правилам:
• приоритетными являются ключи того словаря, сумма значений ключей
которого больше (если суммы значений ключей будут равны, то второй
словарь считается более приоритетным)
• ключи со значениями меньше 10 не должны попасть в финальный
словарь
• получившийся словарь должен вернуться упорядоченным по значениям
ключей в порядке возрастания.

Тесты для примеров и проверки:
connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }) # =>
{ "c": 11, "b": 12 }
connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) # =>
{ d: 11, "c": 12, "a": 13 }
connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }) # =>
{ "c": 11, "b": 12, "a": 15 }
'''


def connect_dicts(dict1, dict2):
    # Вычисляем суммы значений ключей в обоих словарях
    sum1 = sum(value for value in dict1.values() if isinstance(value, (int, float)))
    sum2 = sum(value for value in dict2.values() if isinstance(value, (int, float)))

    # Устанавливаем приоритетный словарь на основе суммы значений
    if sum1 > sum2:
        priority_dict = dict1
        secondary_dict = dict2
    else:
        priority_dict = dict2
        secondary_dict = dict1

    # Создаем результатирующий словарь, исключая значения меньше 10
    result = {}

    for k, v in priority_dict.items():
        if v >= 10:
            result[k] = v

    for k, v in secondary_dict.items():
        if v >= 10 and k not in result:
            result[k] = v

    # Возвращаем отсортированный словарь по значениям
    return dict(sorted(result.items(), key=lambda item: item[1]))


# Тесты
print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))  
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))  
