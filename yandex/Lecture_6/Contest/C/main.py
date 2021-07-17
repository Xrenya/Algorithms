with open('input.txt') as f:
    lines = f.readlines()
    w, h, n = map(int, lines[0].split())

def lbinsearch(w, h, n):
    left = max(w, h) 
    right = left * n
    while right - left > 1:
        middle = (left + right) // 2
        res = (middle // w) * (middle // h)
        if res < n:
            left = middle
        else:
            right = middle
    return round(right)

def min_size(w, h, n):
    size = lbinsearch(w, h, n)
    return size

if __name__ == '__main__':
    size = min_size(w, h, n)
    with open('output.txt', 'w') as file:
        file.write(f"{size}")
