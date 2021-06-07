N = int(input())
array = [int(x) for x in input().split()]
def place(array, N):
    crt = {}
    for i, num in enumerate(array):
        if num % 10 == 5:
            crt[num] = i
    if len(crt) == 0:
        return 0
    winner = -1
    place_1 = max(array)
    place_1_idx = array.index(max(array))
    for val, index in crt.items():
        next_id = index+1
        if next_id < len(array):
            if place_1_idx < index and val > array[next_id]:
                if winner < val:
                    winner = val

    if winner == -1:
        return 0
    else:
        array = sorted(array, reverse=True)
        ans = array.index(winner) + 1
        return ans
            
print(place(array, N))
