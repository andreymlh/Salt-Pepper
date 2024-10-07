'''
Анаграмма — литературный приём, состоящий в перестановке букв или звуков
определённого слова (или словосочетания), что в результате даёт другое слово
или словосочетание.
Разработайте метод combine_anagrams(words_array), который принимает на вход
массив слов и разбивает их в группы по анаграммам, регистр букв не имеет
значения при определении анаграмм.

Тест для примеров и проверки:
combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]) # => [ ["cars", "racs", "scar"], ["four"], ["for"],
["potatoes"], ["creams", "scream"] ]"
'''

def combine_anagrams(words_array):
    anagrams = {}
    
    for word in words_array:
        # Приводим слово к нижнему регистру и сортируем его символы
        sorted_word = ''.join(sorted(word.lower()))
        
        # Добавляем слово в соответствующую группу анаграмм
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    
    # Возвращаем все группы анаграмм как список списков
    return list(anagrams.values())

# Тест
result = combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
                           "creams", "scream"])
print(result)
