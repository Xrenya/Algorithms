num = int(input())
arr = [str(x) for x in input().split()]
last = arr.pop()
arr.insert(0, last)

print(" ".join(arr))
