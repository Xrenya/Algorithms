def two_sum(array, target):
    prevnum = set()
    for nownum in array:
        if target - nownum in prevnum:
            return nownum, target - nownum 
        prevnum.add(nownum)
    return 0, 0
