k = int(input())
s = input()
prevlen = 0
ans = 0
for i in range(k, len(s)):
    if s[i] == s[i - k]:
        prevlen += 1
        ans += prevlen
    else:
        prevlen = 0
print(ans)
