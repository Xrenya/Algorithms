def int_repr(l):
    if not l:
        return 0
    return int("".join(map(str, l)))


def solution(l):
    l = sorted(l, reverse=True)
    n = len(l)
    acc = sum(l)
    if acc % 3 == 0:
        return int_repr(l)
    elif acc % 3 == 1:
        i = n - 1
        while i >= 0:
            if l[i] % 3 == 1:
                return int_repr(l[:i] + l[i+1:])
            i -= 1
        i = n - 1
        while i >= 0:
            if l[i] % 3 == 2:
                break
            i -= 1
        j = i - 1
        while j >= 0:
            if l[j] % 3 == 2:
                break
            j -= 1
        return int_repr(l[:j] + l[j+1:i] + l[i+1:])
    else:
        i = n - 1
        while i >= 0:
            if l[i] % 3 == 2:
                return int_repr(l[:i] + l[i+1:])
            i -= 1
        i = n - 1
        while i >= 0:
            if l[i] % 3 == 1:
                break
            i -= 1
        j = i - 1
        while j >= 0:
            if l[j] % 3 == 1:
                break
            j -= 1
        return int_repr(l[:j] + l[j+1:i] + l[i+1:])


print(solution([3, 1, 4, 1, 5, 9]))
