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
def multiply_numbers(inputs=None):  # Добавлен аргумент по умолчанию
    if inputs is None or inputs == '':  # Проверка на None и пустую строку
        return None

    # Проверка на числовые типы
    if isinstance(inputs, (int, float)):
        inputs = str(inputs)  # Превращаем число в строку

    # Проверка на строку
    if isinstance(inputs, str):
        product = 1
        found_digit = False

        for char in inputs:
            if char.isdigit():  # Проверяем, является ли символ цифрой
                product *= int(char)  # Умножаем на цифру
                found_digit = True

        return product if found_digit else None

    # Обработка списка
    elif isinstance(inputs, list):
        product = 1
        found_digit = False
        
        for item in inputs:
            if isinstance(item, (int, float)):  # Проверка на числовые элементы
                for char in str(item):
                    if char.isdigit():
                        product *= int(char)
                        found_digit = True

        return product if found_digit else None

    return None  # Если входные данные не являются строкой или списком

# Тесты
print(multiply_numbers())              
print(multiply_numbers('ss'))           
print(multiply_numbers('1234'))          
print(multiply_numbers('sssdd34'))       
print(multiply_numbers(2.3))             
print(multiply_numbers([5, 6, 4]))       

