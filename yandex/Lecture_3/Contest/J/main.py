def extend(rect, d):
    minPlust, maxPlust, minPlust, maxPlus = rect
    return [minPlust - d, maxPlust + d,
            minPlust - d, maxPlus + d]

def intersect(rect1, rect2):
    ans = [max(rect1[0], rect2[0]), min(rect1[1], rect2[1]),
           max(rect1[2], rect2[2]), min(rect1[3], rect2[3])]
    return ans

t, d, n = map(int, input().split())
posRect = (0, 0, 0, 0)
for _ in range(n):
    posRect = extend(posRect, t)
    navX, navY = map(int, input().split())
    navRec = extend((navX + navY, navX + navY,
                     navX - navY, navX - navY), d)
    posRect = intersect(posRect, navRec)

points = []
for xPlusY in range(posRect[0], posRect[1] + 1):
    for xMinuxY in range(posRect[2], posRect[3] + 1):
        if (xPlusY + xMinuxY) % 2 == 0:
            x = (xPlusY + xMinuxY) // 2
            y = xPlusY - x
            points.append((x, y))

print(len(points))
for point in points:
    print(*point)
