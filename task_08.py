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
    # Проверяем, является ли входной аргумент числом
    if isinstance(inputs, (int, float)):
        inputs = str(inputs)  # Превращаем число в строку

    # Проверяем, является ли входной аргумент строкой
    if isinstance(inputs, str):
        product = 1
        found_digit = False

        for char in inputs:
            if char.isdigit():  # Проверяем, является ли символ цифрой
                product *= int(char)  # Умножаем на цифру
                found_digit = True

        return product if found_digit else None

    # Если входные данные - это список
    elif isinstance(inputs, list):
        product = 1
        found_digit = False
        
        for item in inputs:
            if isinstance(item, (int, float)):
                for char in str(item):
                    if char.isdigit():
                        product *= int(char)
                        found_digit = True

        return product if found_digit else None

   
    return None

# Тесты
print(multiply_numbers(None))               
print(multiply_numbers('ss'))                
print(multiply_numbers('1234'))              
print(multiply_numbers('sssdd34'))           
print(multiply_numbers(2.3))                 
print(multiply_numbers([5, 6, 4]))           

