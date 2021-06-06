a, b, c, d = list(map(int, input().split(" ")))
def dim(a, b, c, d):
    square = 0
    ans = []
    dim1 = max(b, c) * (a + d)
    ans.append([max(b, c), (a + d)])
    dim2 = max(b, d) * (a + c)
    ans.append([max(b, d), (a + c)])
    dim3 = max(a, d) * (b + c)
    ans.append([max(a, d), (b + c)])
    dim4 = max(a, c) * (b + d)
    ans.append([max(a, c), (b + d)])
    min_square = min(dim1, dim2, dim3, dim4)
    for i, num in enumerate([dim1, dim2, dim3, dim4]):
        if num == min_square:
            print(ans[i][0], ans[i][1])
            break

dim(a, b, c, d)
