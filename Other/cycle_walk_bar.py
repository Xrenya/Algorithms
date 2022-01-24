import pytest


def solution(nums):
    if len(nums) == 0:
        return 0
    slow, fast = nums[0], nums[0]
    # Find the entry point into cycle
    while True:
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast:
            break
    # Count cycle len
    visited = [False] * len(nums)
    cnt = 0
    while visited[slow] is False:
        visited[slow] = True
        slow = nums[slow]
        cnt += 1
    return cnt


@pytest.mark.parametrize(
    "input, output",
    [
        ([1, 0], 2),
        ([1, 2, 1], 2),
        ([1, 3, 0, 1], 2),
        ([1, 2, 3, 4, 0], 5),
    ]
)
def test_solution(input, output):
    out = solution(input)
    assert out == output, (
        f"The function output is expected {output}, but got {out}"
    )

