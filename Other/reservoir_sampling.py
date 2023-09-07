# Алгоритм резервуарной выборки
# Резервуарная выборка (eng. «reservoir sampling») — это простой и эффективный алгоритм случайной выборки
# некоторого количества элементов из имеющегося вектора большого и/или неизвестного заранее размера.


import random

# size, iterable
# size <= iterable
# random.random() ~ U(0, 1)


def select_k_items(iterable, size):
    n = len(iterable)
    reservoir = [0] * size
    for i in range(size):
        reservoir[i] = iterable[i]
    i = size
    while i < n:
        j = random.randrange(i + 1)
        if j < size:
            reservoir[j] = iterable[i]
        i += 1
    return reservoir

iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = 3
print(select_k_items(iterable, size))
