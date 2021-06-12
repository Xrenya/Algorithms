array_1 = set(map(int, input().split()))
array_2 = set(map(int, input().split()))
 
intersection = sorted(list(array_1.intersection(array_2)))

print(" ".join(map(str, intersection)))
