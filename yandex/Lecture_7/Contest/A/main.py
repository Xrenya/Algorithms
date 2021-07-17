with open('input.txt') as f:
    N, K = list(map(int, f.readline().split()))
    num_n = sorted(list(map(int, f.readline().split())))
    num_k = list(map(int, f.readline().split()))

def binary(array, target):
    low, high = 0, len(array)
    while low < high:
        middle = (high + low) // 2
        if array[middle] == target:
            return True
        elif array[middle] > target:
            high = middle
        else:
            low = middle + 1
    return False


def runner(N, K, num_n, num_k):
    output = []
    for i in range(K):
        if binary(num_n, num_k[i]):
            output.append("YES")
        else:
            output.append("NO")
    return "\n".join(output)

if __name__ == '__main__':
    ans = runner(N, K, num_n, num_k)
    with open('output.txt', 'w') as file:
        file.write(f"{ans}")
