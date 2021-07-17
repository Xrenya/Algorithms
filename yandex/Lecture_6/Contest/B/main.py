with open('input.txt') as f:
    N, K = list(map(int, f.readline().split()))
    num_n = list(map(int, f.readline().split()))
    num_k = list(map(int, f.readline().split()))

def lbinsearch(array, target):
    left, right = 0, len(array) - 1
    while left < right:
        middle = (left + right) // 2
        if array[middle] > target:
            right = middle
        else:
            left = middle + 1
    if left == 0:
        return array[left]
    if abs(array[left - 1] - target) <= abs(array[left] - target):
        return array[left - 1]
    return array[left]

def approximation(N, K, num_n, num_k):
    output = []
    for i in range(K):
        closest = lbinsearch(num_n, num_k[i])
        output.append(str(closest))
    return "\n".join(output)

if __name__ == '__main__':
    ans = approximation(N, K, num_n, num_k)
    with open('output.txt', 'w') as file:
        file.write(f"{ans}")
