def calc():
    array = list(map(int, input().split()))
    num = int(input())
    hashMap = {}
    for n in array:
        if n not in hashMap:
            hashMap[n] = 0
        hashMap[n] += 1

    cnt = 0
    seen = {}
    while num != 0:
        last = num % 10
        num //= 10

        if last not in hashMap and last not in seen:
            seen[last] = 0
            cnt += 1
    return cnt

print(calc())
