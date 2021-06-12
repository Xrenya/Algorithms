cnt = int(input())
array = []
for _ in range(cnt):
    array.append(list(map(int, input().split())))

def angrybird():
    hashBird = {}
    for x, y in array:
        if x not in hashBird:
            hashBird[x] = 0
        hashBird[x] += 1
    return len(hashBird)

print(angrybird())
