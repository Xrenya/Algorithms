# https://codeforces.com/group/dAhOSPf3oD/contest/349149/problem/A

def selection_sort():
    n = int(input())
    a = list(map(int, input().strip().split()))
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
            
    print(*a)


def insertation_sort():
    n = int(input())
    a = list(map(int, input().strip().split()))
    
    for i in range(n):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
            
    print(*a)


def merge_sort():
    n = int(input())
    a = list(map(int, input().strip().split()))

    def merge(left, right):
        output = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                output.append(left[l])
                l += 1
            else:
                output.append(right[r])
                r += 1

        if l < len(left):
            output.extend(left[l:])
        if r < len(right):
            output.extend(right[r:])
        return output
        
    def sort(a):
        if len(a) <= 1:
            return a
        pivot = len(a) // 2
        left = sort(a[:pivot])
        right = sort(a[pivot:])
        return merge(left, right)
    
    return sort(a)
print(*merge_sort())
