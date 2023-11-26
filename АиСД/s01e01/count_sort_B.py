n = int(input())
a = list(map(int, input().strip().split()))


def count_sort(a):
    bin = [0] * 101

    for val in a:
        bin[val] += 1

    output = []
    for n in range(len(bin)):
        if bin[n] > 0:
            output.extend([n] * bin[n])

    return output

print(*count_sort(a))
