n, k = map(int, input().split())
x = list(map(int, input().split()))
cntnums = {}
for now in x:
    if now not in cntnums:
        cntnums[now] = 0
    cntnums[now] += 1
uniqnums = list(cntnums.keys())
uniqnums.sort()
r = 0
ans = 0
duplicates = 0
for l in range(len(uniqnums)):
    while r < len(uniqnums) and uniqnums[l] * k >= uniqnums[r]:
        if cntnums[uniqnums[r]] >= 2:
            duplicates += 1
        r += 1
    rangelen = r - l
    if cntnums[uniqnums[l]] >= 2:
        ans += (rangelen - 1) * 3 
    if cntnums[uniqnums[l]] >= 3:
        ans += 1
    ans += (rangelen - 1) * (rangelen - 2) * 3
    if cntnums[uniqnums[l]] >= 2:
        duplicates -= 1
    ans += duplicates * 3
print(ans)
