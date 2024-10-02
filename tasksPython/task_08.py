'''
Написать метод multiply_numbers(inputs), который вернет произведение цифр,
входящих в inputs.

Тест для примеров и проверки:
multiply_numbers() # => None
multiply_numbers('ss') # => None
multiply_numbers('1234') # => 24
multiply_numbers('sssdd34') # => 12
multiply_numbers(2.3) # => 6
multiply_numbers([5, 6, 4]) # => 120
'''
def multiply_numbers(inputs):
    # Проверяем на None и на соответствия типов
    if inputs is None or not isinstance(inputs, (str, list, int, float)):
        return None

    product = 1
    found_digit = False

    # Если входные данные - строка
    if isinstance(inputs, str):
        for char in inputs:
            if char.isdigit():  # Проверяем, является ли символ цифрой
                product *= int(char)
                found_digit = True

    # Если входные данные - список
    elif isinstance(inputs, list):
        for item in inputs:
            if isinstance(item, (int, float)):  # Проверяем, является ли элемент числом
                digits = str(int(item))  # Убираем дробную часть и превращаем в строку
                for char in digits:
                    product *= int(char)
                    found_digit = True

    # Если входные данные - число (int или float)
    elif isinstance(inputs, (int, float)):
        digits = str(int(inputs))  
        for char in digits:
            product *= int(char)
            found_digit = True

    
    return product if found_digit else None

# Тесты
print(multiply_numbers(None))         
print(multiply_numbers('ss'))         
print(multiply_numbers('1234'))       
print(multiply_numbers('sssdd34'))    
print(multiply_numbers(2.3))          
print(multiply_numbers([5, 6, 4]))   
