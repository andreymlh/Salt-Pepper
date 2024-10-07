'''
Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
принимающим на вход name и calories (не обязательные параметры), а также двумя
методами is_healthy (возвращает true при условии калорийности десерта менее
200) и is_delicious (возвращает true для всех десертов).
'''

class Dessert:
    def __init__(self, name=None, calories=0):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = value

    def is_healthy(self):
        return self._calories < 200

    def is_delicious(self):
        return True

# Примеры использования
dessert1 = Dessert("Chocolate Cake", 350)
dessert2 = Dessert("Fruit Salad", 150)

print(dessert1.name)        
print(dessert1.calories)    
print(dessert1.is_healthy())  
print(dessert1.is_delicious()) 

print(dessert2.name)        
print(dessert2.calories)    
print(dessert2.is_healthy())  
print(dessert2.is_delicious()) 
