def iterator_without_yield(n):
    return (i for i in range(1, n) if i % 2 != 0 and i**2 < 200)

gen1 = iterator_without_yield(11)

for i in gen1:
    print(i)
next(gen1)



