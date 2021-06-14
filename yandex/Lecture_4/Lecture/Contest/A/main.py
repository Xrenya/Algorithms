array = []
for i in range(int(input())):
    array += input().split()
find = input()
idx = array.index(find)
if idx % 2 == 0:
    print(array[idx+1])
else:
    print(array[idx-1])
