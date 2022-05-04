# 5. Задание
numbers = [57.8, 46.51, 97, 50, 22.3, 12, 44.7, 5.2, 68, 10, 55.5, 85.15, 72.45, 60, 30.7]
print(f'\tИсходный список:\n{numbers}')
# Часть А
for number in numbers:
    rub = number
    cop = (number * 100) % 100
    if type(number) == int:
        number =  f'{rub:.0f} руб {cop:02} коп'
    elif type(number) == float:
        number = f'{rub:.0f} руб {cop:.0f} коп'
    print(number, end=', ')

# Часть В
print('\nДоказательство операции in place:')
print(f'\tid перед сортировкой {id(numbers)}')
numbers.sort()
print(f'\tid после сортировкой {id(numbers)}')

# Часть C
numbers_reverse = sorted(numbers, reverse=True)
print(numbers_reverse)
print(f'\tid после сортировкой {id(numbers_reverse)}')

# Часть D
print('5 самых дорогих товаров:')
for numbers_max in numbers_reverse[0:5]:
    print(f'\t{numbers_max}')
