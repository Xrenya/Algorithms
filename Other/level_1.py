from collections import Counter


def solution(data, n):
    if n == 0:
        return []

    task_hash = Counter(data)
    output = []
    for num in data:
        if task_hash[num] <= n:
            output.append(num)
    print(output)
    return output

solution([1,2, 3, 3, 2, 2, 2, 1], 2)
# [1,2, 3, 3, 2, 2, 2, 1] -> [1, 3, 3, 1]
