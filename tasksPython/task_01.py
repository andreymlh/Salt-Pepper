'''
Разработайте метод is_palindrome(string), который будет определять, является ли 
параметр string палиндромом (строкой, которая читается одинаково как сначала так и сконца),
при условии игнорирования пробелов, знаков препинания и регистра.

Тесты для примеров и проверки:
is_palindrome("A man, a plan, a canal -- Panama") # => True
is_palindrome("Madam, I'm Adam!") # => True
is_palindrome(333) # => True
is_palindrome(None) # => False
is_palindrome("Abracadabra") # => False#
'''

import re

def is_palindrome(string):
    if string is None:
        #string = input("Введите строку для проверки на палиндром: ")
        return False
    
    # Приведение к строке и удаление не буквенно-цифровых символов
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', str(string)).lower()
    
    # Проверка, является ли очищенная строка палиндромом
    return cleaned_string == cleaned_string[::-1]

# Тесты
print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))                         
