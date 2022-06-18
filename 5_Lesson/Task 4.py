src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

lst = [src[x] for x in range(len(src)) if src[x] > src[x-1]]

print(lst)