# Given a list of of dates represet as iteger (0, 1], (1, 2], (1, 4]

# Those represent check-in(inclusive) and check-out(exclusive) timestemp
# Find the maximum number of rooms which would fit everyone

# Solution should be faster when O(n^2)
                                                             
def load(s):
    l = []
    for check_in, check_out in s:
        l.append((check_in, 1))
        l.append((check_out, -1))

    l.sort()
    max_load, cur = 0, 0
    for t, n in l:
        cur += n
        max_load = max(max_load, cur)

    return max_load
