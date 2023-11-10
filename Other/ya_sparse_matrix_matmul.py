# sudo-sparse matrix muplication
# a = [1,1,2] -> a = [(1, 2), (2, 1)] (value, count)
# b = [1,1,1] -> b = [(1, 3)]
# matrix multiplication

def matmul(a, b):
    # verify that two vector is actually possible to matmul
    size_a = sum([x[1] for x in a])
    size_b = sum([x[1] for x in b])
    if size_a != size_b:
        return -1

    acc = 0
    a_idx = 0
    b_idx = 0
    a_count, b_count = 0, 0
    while a_idx < len(a) or b_idx < len(b):
        if a_count == 0:
            val_a, a_count = a[a_idx]
            a_idx += 1
        if b_count == 0:
            val_b, b_count = b[b_idx]
            b_idx += 1
        max_count = min(a_count, b_count)
        acc = acc + (val_a * val_b) * max_count
        a_count, b_count = a_count - max_count, b_count - max_count
    return acc

a = [(1, 2), (2, 1), (2, 1)]
b = [(1, 3), (3, 1)]
assert matmul(a, b) == 10


a = [(1, 2), (2, 1)]
b = [(1, 3)]
assert matmul(a, b) == 4

a = [(1, 2), (2, 2)]
b = [(1, 3)]
assert matmul(a, b) == -1
