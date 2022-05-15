str1 = ["Иван Сергеев", "Алла Сидорова", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков"]
i = 0
dct1 = {}
str1 = sorted(str1)

for x in str1:
    name, surname = str1[i].split()
    name_2 = name
    name = surname
    surname = name_2
    if surname[0] not in dct1:
        dct1[surname[0]] = {}
        dct1[surname[0]].setdefault(name[0], []).append(f'{name} {surname}')
    else:
        if name[0] and surname[0] in dct1:
            dct1[surname[0]].setdefault(name[0], []).append(f'{name} {surname}')
        else:
            dct1[surname[0]][name[0]] = [str1[i]]
    i += 1

print(dct1)
