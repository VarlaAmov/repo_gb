import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(jokes_count, lst1=nouns, lst2=adverbs, lst3=adjectives):
    """
    :param jokes_count: Параметр определяющий количество выводимых шуток
    :param lst1: Параметр списка 'nouns', содержимое выводимой шутки зависит от содержания списка 'nouns'
    :param lst2: Параметр списка 'adverbs', содержимое выводимой шутки зависит от содержания списка 'adverbs'
    :param lst3: Параметр списка 'adjectives', содержимое выводимой шутки зависит от содержания списка 'adjectives'
    :return: Возвращает скомпелированные шутки в функцию 'get_jokes'
    """
    lst_prefinal = []
    lst_final = []
    i = 0
    j = 0

    while i < jokes_count:
        r = random.randint(0, len(lst1) - 1)
        lst_prefinal.append(lst1[r])
        lst_prefinal.append(lst2[r])
        lst_prefinal.append(lst3[r])
        lst_final.append(f'{lst_prefinal[j]} {lst_prefinal[j+1]} {lst_prefinal[j+2]}')
        i += 1
        j += 3

    return lst_final


print(get_jokes(3, nouns, adverbs, adjectives))
print(get_jokes(3))
