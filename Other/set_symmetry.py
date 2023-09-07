# //Дан массив точек с целочисленными координатами (x, y).
# //Определить, существует ли вертикальная прямая, делящая точки на 2 симметричных относительно этой прямой множества.
# //Note: Для удобства точку можно представлять не как массив [x, y], а как объект {x, y}


def isSymmetrical(points):
    pmax, pmin = points[0][0], points[0][0]
    mp = {}
    for p in points:
        if p[0] > pmax:
            pmax = p[0]
        if p[0] < pmin:
            pmin = p[0]

        mp[f"{p[0]}.{p[1]}"] = True
        c = pmin + pmax

    for p in points:
        key = f"{c - p[0]}.{p[1]}"
        if not mp.get(key, False):
            return False
    return True

points = [[-1, 1], [1, 1], [2, 0]]
assert isSymmetrical(points) is False

points = [[-1, 1], [1, 1], [0, 0]]
assert isSymmetrical(points) is True

points = [[-1, 1], [1, 1], [-2, 0], [2, 0]]
assert isSymmetrical(points) is True

points = [[-1, 1], [1, 1], [-2, 0], [2, 1]]
assert isSymmetrical(points) is False


