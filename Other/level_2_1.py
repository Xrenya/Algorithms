import pytest


def solution(s: str):
    right = 0
    cnt = 0
    for c in s:
        if c == "<":
            if right > 0:
                cnt += right * 2
        elif c == ">":
            right += 1

    return cnt


@pytest.mark.parametrize(
    "input, output",
    [
        (">----<", 2),
        ("<<>><", 4),
        ("<<>>", 0),
        ("<-->", 0),
        ("----", 0),
        (">><<", 8),
        (">---->", 0),
    ]
)
def test_solution(input, output):
    out = solution(input)
    assert out == output, (
        f"The function output is expected {output}, but got {out}"
    )
