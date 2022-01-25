import pytest


def solution(data):

    cur_set = set()
    for word in data:
        reverse = word[::-1]
        if word not in cur_set and reverse not in cur_set:
            cur_set.add(word)

    return len(cur_set)


@pytest.mark.parametrize(
    "input, output",
    [
        (["foo", "bar", "oof", "bar"], 2),
        (["x", "y", "xy", "yy", "", "yx"], 5),
        (["foo", "bar", "oof", "bar", "rab", ""], 3),
        (["foo", "bar", "oof", "bar", "rab", "", "ofo"], 4),
    ]
)
def test_solution(input, output):
    out = solution(input)
    assert out == output, (
        f"The function output is expected {output}, but got {out}"
    )

