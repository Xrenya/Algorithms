def slow(seq):
    for start in range(len(seq)):
        i = start
        j = len(seq) - 1
        while i < len(seq) and j >= 0 and seq[i] == seq[j] and i <= j:
            i += 1
            j -= 1
        if i > j:
            ans = []
            for i in range(start -1, -1, -1):
                ans.append(seq[i])
            return ans
output = slow([1, 1, 2, 1, 1, 1]) 
print(len(output))
print(*output)
