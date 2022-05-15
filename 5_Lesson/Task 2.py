def iterator_with_yield(n):
    j = 0
    for i in range(1, n):
        if i % 2 != 0 and i**2 < 200:
            yield i, j + i
            j += i

gen1 = iterator_with_yield(14)

for i in gen1:
    print(i)
next(gen1)

