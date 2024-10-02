'''
Разработать метод date_in_future(integer), который вернет дату через integer дней.
Если integer не является целым числом, то метод должен вывести текущую дату.
Формат возвращаемой методом даты должен иметь следующий вид '01-01-2001
22:33:44’.

Тесты для примеров и проверки:
date_in_future([]) # => текущая дата
date_in_future(2) # => текущая дата + 2 дня
'''

from datetime import datetime, timedelta

def date_in_future(days):
    # Проверка, является ли days целым числом
    if not isinstance(days, int):
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    # Если days является целым числом, вычисляем новую дату
    future_date = datetime.now() + timedelta(days)
    
    return future_date.strftime('%d-%m-%Y %H:%M:%S')

# Тесты
print(date_in_future([])) 
print(date_in_future(2))   
