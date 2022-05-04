import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(jokes_count, lst1=nouns, lst2=adverbs, lst3=adjectives, true_or_false=bool):
    lst_prefinal = []
    lst_final = []
    i = 0
    j = 0
    if true_or_false == False:
        r = random.randint(0, len(lst1) - 1)
        while i < jokes_count:
            lst_prefinal.append(lst1[r]), lst_prefinal.append(lst2[r]), lst_prefinal.append(lst3[r])
            lst_final.append(f'{lst_prefinal[j]} {lst_prefinal[j+1]} {lst_prefinal[j+2]}')
            i += 1
            j += 3
        return lst_final
    else:
        if jokes_count <= len(nouns):
            a = list(range(len(nouns)))
            b = list(range(len(adverbs)))
            c = list(range(len(adjectives)))
            random.shuffle(a), random.shuffle(b), random.shuffle(c)
            while i < jokes_count:
                lst_prefinal.append(lst1[a[i]]), lst_prefinal.append(lst2[b[i]]), lst_prefinal.append(lst3[c[i]])
                lst_final.append(f'{lst_prefinal[j]} {lst_prefinal[j + 1]} {lst_prefinal[j + 2]}')
                i += 1
                j += 3
            return lst_final
        else:
            return f'Указанное количество шуток невозможно создать\nДоступное количество: {len(nouns)} '

# print(get_jokes(5, nouns, adverbs, adjectives))
print(get_jokes(10,true_or_false=False))
print(get_jokes(10,true_or_false=True))
print(get_jokes(5,true_or_false=True))


