with open('input.txt') as f:
    limit = int(f.readline().split()[0])
    string = str(f.readline().split()[0])


def operator(limit, string):
    hashMap = {}
    for s in string:
        if s not in hashMap:
            hashMap[s] = 0
        hashMap[s] += 1
    lst = sorted(hashMap.items(), key=lambda item: item[1])
    cnt = 0
    lenght = len(lst)
    for l in range(lenght):
        for r in range(l+1, lenght):
            if lst[l][1] + lst[r][1] > limit:
                cnt += lenght - r
                break
    return cnt

if __name__ == '__main__':
    ans = operator(limit, string)
    with open('output.txt', 'w') as file:
        file.write(f"{ans}")
