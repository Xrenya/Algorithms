with open('input.txt') as f:
    n, r = list(map(int, f.readline().split()))
    nums = list(map(int, f.readline().split()))

def distance(n, r, nums):
    i, j, cnt = 0, 1, 0

    while (i < n - 1) and (j < n):
        if nums[j] - nums[i] <= r:
            j += 1
        else:
            cnt += n - j
            i += 1
    return cnt


if __name__ == '__main__':
    ans = distance(n, r, nums)
    print(ans)
    with open('output.txt', 'w') as file:
        file.write(f"{ans}")
