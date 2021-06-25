with open('input.txt') as f:
    up_num = int(f.readline())
    upper_nums = list(map(int, f.readline().split()))
    low_num = int(f.readline())
    lower_nums = list(map(int, f.readline().split()))


def min_distance(up_num, upper_nums, low_num, lower_nums):
    up = 0
    low = 0
    dif = 10**6
    flag_low = True
    flag_up = True
    best = [upper_nums[0], lower_nums[0]]
    while up < len(upper_nums) and low < len(lower_nums):
        d = abs(upper_nums[up] - lower_nums[low])
        if d == 0:
            return [upper_nums[up], lower_nums[low]]
        else:
            if dif > d:
                dif = d
                best = [upper_nums[up], lower_nums[low]]
            if upper_nums[up] <= lower_nums[low]:
                up += 1
            else:
                low += 1
    return best

if __name__ == '__main__':
    ans = min_distance(up_num, upper_nums, low_num, lower_nums)
    with open('output.txt', 'w') as file:
        file.write(f"{ans[0]} {ans[1]}")
