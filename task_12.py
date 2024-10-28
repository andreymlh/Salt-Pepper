'''
Создайте класс JellyBean, расширяющий класс Dessert (из Упражнения 11) новым
геттером и сеттером для атрибута flavor (все параметры являются не
обязательными). Измените метод is_delicious таким образом, чтобы он возвращал
false только в тех случаях, когда flavor равняется «black licorice».
'''
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
        if isinstance(self._calories, (int, str)) and str(self._calories).isdigit():
            return int(self._calories) < 200
        return False
    
    
class JellyBean(Dessert):
    def __init__(self):
        super().__init__()
        self._flavor = ""  

    @property
    def flavor(self):
        return self._flavor  

    @flavor.setter
    def flavor(self, value):
        if not isinstance(value, str):
            raise ValueError("Flavor must be a string")
        self._flavor = value

    def is_delicious(self):
        #return self._flavor.lower() != "black licorice"
        return str(self._flavor).lower() != "black licorice"

# Тестирование 
dessert = Dessert()
dessert.name = "test_name"
print(dessert.name)
dessert.name = "test_name2"
print(dessert.name)
if dessert.name != "test_name2": raise Exception("Setter for name is not working")

dessert.calories = 350 
print(dessert.calories)  
dessert.calories = "150"  
print(dessert.calories)  

print(dessert.is_delicious())
print(dessert.is_healthy())  

# 12
jelly_bean = JellyBean()
jelly_bean.name = "Test Jelly Bean"
jelly_bean.calories = 100
jelly_bean.flavor = "black licorice"

print(jelly_bean.name)  
print(jelly_bean.calories)  
print(jelly_bean.flavor)  
print(jelly_bean.is_delicious())  

jelly_bean.flavor = "strawberry"
print(jelly_bean.is_delicious())

