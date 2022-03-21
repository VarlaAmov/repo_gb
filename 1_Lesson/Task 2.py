# 2 Задание.
print('Часть а:')
numbers = [x ** 3 for x in range(1, 1000, 2)]
count = 0
for res1 in numbers:
    summ = sum(map(int, str(numbers[count])))
    if summ % 7 == 0:
        print(res1, end=',')
    count += 1

print('\nЧасть b:')
numbers = [x ** 3 for x in range(1, 1000, 2)] 
count = 0
for res1 in numbers:
    res2 = numbers[count] + 17
    summ = sum(map(int, str(res2)))
    if summ % 7 == 0:
        print(res2, end=',')
    count += 1


