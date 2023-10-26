def rle(arr):
    if len(arr) <= 1:
        return arr
    prev = arr[0]
    output = [prev]
    for i in range(1, len(arr)):
        if prev == arr[i]:
            continue
        prev = arr[i]
        output.append(prev)
    return output

assert rle(["A", "A", "A", "B", "C", "C"]) == ["A", "B", "C"]
