import pytest


def solution(nums, target):
    left = 0
    acc = 0
    for right in range(0, len(nums)):
        acc += nums[right]
        while acc > target:
            acc -= nums[left]
            left += 1
        if acc == target:
            return [left, right]
    return [-1, -1]


@pytest.mark.parametrize(
    "input, output",
    [
        (([4, 3, 10, 2, 8], 12), [2, 3]),
        (([1, 2, 3, 4], 15), [-1, -1]),
        (([], 15), [-1, -1]),
        (([1, 2, 3], 3), [0, 1]),
        (([1, 2, 3], 1), [0, 0]),
        (([1, 2, 3, 4], 10), [0, 3]),
    ]
)
def test_solution(input, output):
    out = solution(*input)
    assert out == output, (
        f"The function output is expected {output}, but got {out}"
    )
