# ["x", "y", "0"]
# "x000y" -> 4
# "yx" -> 1
# "x000y0x" -> 2
# "xx0y -> 2

# min_range = float("inf")
# x/y - > last x -> x, xy -> 1, x000y 

def min_range_measure(string: str) -> int:
    min_range = float("inf")
    index = 0
    last = None
    for i, s in enumerate(string):
        if last is None and (s == "x" or s == "y"):
            last = s
            index = i
        elif s == last:
            index = i
            continue
        elif s == "0":
            continue
        elif s != last and (s == "x" or s == "y"):
            min_range = min(min_range, i - index)
            last = s
            index = i
    return min_range if min_range != float("inf") else -1
    
# "000" -> -1
# "yx" -> 
# "y" -> index = 0, last="y"; "x" -> i(1) - index(0) = 1,  min_range = 1, last = "x", index=1
# "x000x" -> -1
# "x000y0x" ->    
# "xyxyx"
