N, K, M = list(map(int, input().split()))
def details(N, K, M):
    if K < M:
        return 0
    cnt = 0
    while N >= K:
        N -= K
        cnt += K // M
        left_out = K - K // M * M
        N += left_out
    return cnt

print(details(N, K, M))
