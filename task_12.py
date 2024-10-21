'''
Создайте класс JellyBean, расширяющий класс Dessert (из Упражнения 11) новым
геттером и сеттером для атрибута flavor (все параметры являются не
обязательными). Измените метод is_delicious таким образом, чтобы он возвращал
false только в тех случаях, когда flavor равняется «black licorice».
'''
class Dessert:
    def __init__(self, name=None, calories=0):
        self._name = name
        self._calories = int(calories)

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
        self._calories = int(value)

    def is_healthy(self):
        return self._calories < 200

    def is_delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name=None, calories=0, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        return self._flavor != "black licorice"  

# Примеры использования
jelly_bean1 = JellyBean("Cherry Jellybean", 150, "cherry")
jelly_bean2 = JellyBean("Licorice Jellybean", 150, "black licorice")

print(jelly_bean1.name)          
print(jelly_bean1.calories)      
print(jelly_bean1.flavor)        
print(jelly_bean1.is_healthy())  
print(jelly_bean1.is_delicious()) 

print(jelly_bean2.name)          
print(jelly_bean2.calories)      
print(jelly_bean2.flavor)        
print(jelly_bean2.is_healthy())  
print(jelly_bean2.is_delicious()) 
