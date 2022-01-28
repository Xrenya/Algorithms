import pytest


def solution(s1, s2):
    if abs(len(s1) - len(s2)) >= 2:
        return False

    if len(s1) == 0 or len(s2) == 0:
        if len(s1):
            return len(s1) == 1
        elif len(s2):
            return len(s2) == 1
        return False

    prefix = 0
    while (prefix < len(s1) - 1) or (prefix < len(s2) - 1):
        if s1[prefix] != s2[prefix]:
            break
        prefix += 1

    if prefix == len(s1) and prefix == len(s2):
        return True

    suffix = 0
    while (suffix < len(s1) - 1) or (suffix < len(s2) - 1):
        if s1[len(s1) - 1 - suffix] != s2[len(s1) - 1 - suffix]:
            break
        suffix += 1

    length = len(s1) if len(s1) > len(s2) else len(s2)
    return length - prefix - suffix <= 1


solution("cat", "cct")
@pytest.mark.parametrize(
    "input, output",
    [
        (("", ""), False),
        (("ad", ""), False),
        (("a", ""), True),
        (("", "a"), True),
        (("cat", "cat"), True),
        (("cat", "cct"), True),
        (("cat", "ccc"), False)
    ]
)
def test_solution(input, output):
    assert solution(*input) == output
