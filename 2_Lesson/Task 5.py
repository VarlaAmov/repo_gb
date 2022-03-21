# 5. Задание

numbers = [57.8, 46.51, 97, 50, 22.3, 12, 44.7, 5.2, 68, 10, 55.5, 85.15, 72.45, 60, 30.07]

# Часть А
i = 0

for number in numbers:
    rub = numbers[i]
    cop = (numbers[i] * 100) % 100
    if type(numbers[i]) == int:
        numbers[i] =  f'{rub:.0f} руб {cop:02} коп'
    elif type(numbers[i]) == float:
        numbers[i] = f'{rub:.0f} руб {cop:.0f} коп'
    print(numbers[i], end=', ')
    i += 1

print()

# Часть В
print(id(numbers))
numbers.sort()
print(id(numbers))

# Часть C
numbers_reverse = sorted(numbers, reverse=True)
print(numbers_reverse)

# Часть D

numbers_max = numbers_reverse[0:5]
print(sorted(numbers_max))
