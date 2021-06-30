def check(m, checkparams):
    minbrigades, c, heights = checkparams
    i = 0
    brigades = 0
    while i < len(heights) - c + 1:
        if heights[i + c -1] - heights[i] <= m:
            brigades += 1
            i += c
        else:
            i += 1
    return brigades >= minbrigades

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

n, r, c, = map(int, input().split())
heights = []
for _ in range(n):
    heights.append(int(input()))
heights.sort()
print(lbinsearch(0, heights[-1] - heights[0], check, (r, c, heights)))
