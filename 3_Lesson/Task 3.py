def thesaurus(*kwargs):
    q = {}
    i = 0
    kwargs = sorted(kwargs)
    for x in kwargs:
        if kwargs[i][0]:
            q.setdefault(kwargs[i][0], []).append(kwargs[i])
        i += 1
    return q


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Артем", "Вадим", "Анатолий"))




