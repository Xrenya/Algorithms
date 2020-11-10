Hour1 = int(input())
Min1 = int(input())
Sec1 = int(input())

Hour2 = int(input())
Min2 = int(input())
Sec2 = int(input())

def difference(Hour1, Min1, Sec1, Hour2, Min2, Sec2):
    if Sec1 > Sec2:
        Min2 -= 1
        seconds = Sec2 + 60 - Sec1
    else:
        seconds = Sec2 - Sec1
    if Min1 > Min2:
        Hour2 -= 1
        seconds += (Min2 + 60 - Min1) * 60
    else:
        seconds += (Min2 - Min1) * 60
    seconds += (Hour2 - Hour1) * 3600
    return seconds

print(difference(Hour1, Min1, Sec1, Hour2, Min2, Sec2))
