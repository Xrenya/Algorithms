def getentraceandfloor(flatno, flatsonfloor, floors):
    floorsbefore = (flatno - 1) // flatsonfloor
    entrance = floorsbefore // floors + 1
    floor = floorsbefore % floors + 1
    return entrance, floor
    
def check(k1, m, k2, p2, n2, flatsonfloor):
    entracnce2, floor2 = getentraceandfloor(k2, flatsonfloor, m)
    if entracnce2 == p2 and floor2 == n2:
        return getentraceandfloor(k1, flatsonfloor, m)
    return -1, -1

def slow(k1, m, k2, p2, n2):
    randval = 10**6
    ent = -1
    floor = -1
    goodflag = False
    for flatsonfloor in range(1, randval):
        nent, nfloor = check(k1, m, k2, p2, n2, flatsonfloor)
        if nent != -1:
            goodflag = True
            if ent == -1:
                ent, floor = nent, nfloor
            elif ent != nent and ent != 0:
                ent = 0
            elif floor != nfloor and floor != 0:
                floor = 0
    if goodflag:
        return (ent, floor)
    else:
        return (-1, -1)
        
print(slow(3, 2, 2, 2, 1))
