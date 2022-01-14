sample = [(1, 2), (1, 3), (2, 4), (2, 3),]

event = []
for s in sample:
    start, end = s
    event.append([start, 1])
    event.append([end, -1])

event.sort()
cnt = 0
curr = 0
for e in event:
    curr += e[-1]
    cnt = max(cnt, curr)
print(cnt)
