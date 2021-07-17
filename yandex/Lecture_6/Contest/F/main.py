with open('input.txt') as f:
    N, x, y = list(map(int, f.readline().split()))

def lbinsearch(N, x, y, checker):
    left = 0
    right = min(x, y) * N
    while left < right:
        middle = (left + right) // 2
        if checker(N, x, y, middle):
            right = middle
        else:
            left = middle + 1
    return left

def checker(N, x, y, middle):
    min_speed = min(x, y)
    max_speed = max(x, y)
    pages = middle // min_speed + (middle - min_speed) // max_speed
    return pages >= N


def printer(N, x, y, checker):
    time = lbinsearch(N, x, y, checker)
    return time

if __name__ == '__main__':
    time = printer(N, x, y, checker)
    with open('output.txt', 'w') as file:
        file.write(f"{time}")
