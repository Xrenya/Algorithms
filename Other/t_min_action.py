import pytest


def min_actions(s, n):
    dp = [float('inf') for i in range(n)]

    s1 = ""
    s2 = ""

    # base case
    dp[0] = 1
    s1 += s[0]

    for i in range(1, n):
        s1 += s[i]

        s2 = s[i + 1: i + 1 + i + 1]

        dp[i] = min(dp[i], dp[i - 1] + 1)
        print(s1, s2)
        if (s1 == s2):
            dp[i * 2 + 1] = min(dp[i] + 1, dp[i * 2 + 1])

    return dp[n - 1]



s = "aaaaaaaa"
n = len(s)
@pytest.mark.parametrize(
    "input,output",
    [
        (["aaaaaaaa", n], 4),
        (["aaabaaab", n], 5)
    ]
)
def test_min_actions(input, output):
    actions = min_actions(*input)
    assert actions == output, f"Expected output '{output}', but got '{actions}'"
