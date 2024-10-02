'''
Разработайте функцию count_words(string), которая будет возвращать словарь со
статистикой частоты употребления входящих в неё слов.

Тесты для примеров и проверки:
count_words("A man, a plan, a canal -- Panama") # => {"a": 3, "man": 1,
"canal": 1, "panama": 1, "plan": 1}
count_words("Doo bee doo bee doo") # => {"doo": 3, "bee": 2}
'''

import re
from collections import Counter

def count_words(string):
    # Приводим строку к нижнему регистру и разбиваем на слова с использованием регулярных выражений
    words = re.findall(r'\b\w+\b', string.lower())
    
    # Считаем частоту слов
    word_count = Counter(words)
    
    # Преобразуем Counter в обычный словарь
    return dict(word_count)

# Тесты
print(count_words("A man, a plan, a canal -- Panama"))  
print(count_words("Doo bee doo bee doo"))  
