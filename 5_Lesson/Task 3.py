tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Евгений', 'Максим', 'Яна']
groups = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def func_gen(t, g):
    i = 0
    print(f'Ученики: {t}')
    print(f'Классы: {g}')
    print(f'Тип объекта: {type(func_gen(t, g))}')
    while i < len(t):
        if i >= len(g):
            yield t[i], None
            i += 1
        else:
            yield t[i], g[i]
            i += 1

gen1 = func_gen(tutors, groups)

for i in gen1:
    print(i)