'''
Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
принимающим на вход name и calories (не обязательные параметры), а также двумя
методами is_healthy (возвращает true при условии калорийности десерта менее
200) и is_delicious (возвращает true для всех десертов).
'''
import math

class Dessert:
    def __init__(self):
        self._name = ""
        self._calories = 0 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be string")
        self._name = value

    @property
    def calories(self):
        return self._calories
    
    

    @calories.setter
    def calories(self, value):
        self._calories = value

    def is_delicious(self):
        return True 

    
    def is_healthy(self):
        if type(self._calories) in (int, float) and math.floor(float(self._calories)) < 200:
            return True
        else:
            return False

        

# Тестирование 
dessert = Dessert()
dessert.name = "test_name"
print(dessert.name)
dessert.name = "test_name2"

print(dessert.name)
if dessert.name != "test_name2": raise Exception("Setter for name is not working")

dessert.calories = 350
print(dessert.calories)  
dessert.calories = 199.9999  
print(dessert.calories)  

print(dessert.is_delicious())

print(dessert.is_healthy())  
