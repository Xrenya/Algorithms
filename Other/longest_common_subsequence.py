def lcs(x, y):
    len_x = len(x)
    len_y = len(y)
    dp = [[-1] * (len_y + 1) for _ in range(len_x + 1)]
    for i in range(len_x + 1):
        for j in range(len_y + 1):
            if i == 0 or j == 0:
                dp[i][j] == 0
            elif y[j - 1] == x[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    i = len_x
    j = len_y
    lcs = ""
    while i > 0 and j > 0:

        if x[i - 1] == y[j - 1]:
            lcs += y[j - 1]
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs = lcs[::-1]
    return lcs
