import pytest


def solution(intervals):
    intervals.sort()
    merge = [intervals[0]]
    for inter in intervals[1:]:
        if inter[0] <= merge[-1][1] and inter[1] <= merge[-1][1]:
            continue
        elif inter[0] < merge[-1][1]:
            merge[-1] = [merge[-1][0], inter[1]]
        else:
            merge.append(inter)
    return len(merge)


@pytest.mark.parametrize(
    "input, output",
    [
        ([[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]], 4),
        ([[0, 1000000], [42, 43], [0, 1000000], [42, 43]], 1),
        ([[0, 1000000], [42, 43], [0, 1000000], [42, 43], [1000000, 1000001]], 2),
        ([[0, 1], [1, 2], [2, 3], [3, 5], [4, 5], [0, 10]], 1),
    ]
)
def test_solution(input, output):
    out = solution(input)
    assert out == output, (
        f"The function output is expected {output}, but got {out}"
    )

