with open('input.txt') as f:
    lenght, limit = list(map(int, f.readline().split()))
    string = f.readline().split()[0]


def substring(lenght, limit, string):
    hashMap = {}
    l, r = 0, 0
    cnt = 0
    first = 0
    while l < lenght and r < lenght:
        if string[r] not in hashMap:
            hashMap[string[r]] = 0
        hashMap[string[r]] += 1
        if hashMap[string[r]] > limit:
            nowcnt = r - l
            if nowcnt > cnt:
                cnt = nowcnt
                first = l
                hashMap[string[l]] -= 1
                l += 1
            else:
                hashMap[string[l]] -= 1
                l += 1
        r += 1
    nowcnt = r - l
    if nowcnt > cnt:
        cnt = nowcnt
        first = l
    return [cnt, first+1]

if __name__ == '__main__':
    ans = substring(lenght, limit, string)
    with open('output.txt', 'w') as file:
        file.write(f"{ans[0]} {ans[1]}")
