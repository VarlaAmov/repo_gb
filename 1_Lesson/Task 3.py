# 3 Задание

#--------------------1 Вариант---------------------

#percent = int(input('Введите желаемый процент: '))
#
#if percent == 1:
#    print(percent, 'процент')
#elif percent > 1 and percent < 5:
#    print(percent, 'процента')
#elif percent <= 100:
#    print(percent, 'процентов')



#--------------------2 Вариант---------------------

list_numbers = [i for i in range(1, 101)]

for numbers in list_numbers:
    if numbers == 1:
        print(numbers, 'процент')
    elif 1 < numbers <= 4:
        print(numbers, 'процента')
    elif 4 < numbers <= 100:
        print(numbers, 'процентов')

