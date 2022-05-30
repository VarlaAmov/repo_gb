import os
from os.path import join

rng = [100, 1000, 10000, 100000]
dct = {}
dir1 = join(".", "some_data")

for i in rng:
    x = 0
    for j in os.scandir(dir1):
        if os.path.isfile(j):
            size = os.path.getsize(j)
            if size < i and size > i / 10:
                dct[i] = x + 1
                x += 1
            elif i == 100 and size < 10:
                dct[i] = x + 1
                x += 1

print(dct)