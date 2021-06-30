n = int(input())
points = [] * n
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
ans = 0
for i in range(n):
    usedvectors = set()
    neig = []
    for j in range(n):
        vecx = points[i][0] - points[j][0]
        vecy = points[i][1] - points[j][1]
        veclen = vecx ** 2 + vecy ** 2
        neig.append(veclen)
        if (vecx, vecy) in usedvectors:
            ans -= 1
        usedvectors.add((-vecx, -vecy))
    neig.sort()
    r = 0
    for l in range(len(neig)):
        while r < len(neig) and neig[l] == neig[r]:
            r += 1
        ans += r - l - 1
print(ans)
