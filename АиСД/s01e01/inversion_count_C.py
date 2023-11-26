def insertation_sort_inversion_count():
    n = int(input())
    a = list(map(int, input().strip().split()))
    count = 0
    for i in range(n):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
            count += 1
    return count
print(insertation_sort_inversion_count())  # TL solution
