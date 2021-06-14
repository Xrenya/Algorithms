def freq(hash, word):
    if word not in hash:
        hash[word] = 0
        return hash[word]
    else:
        hash[word] += 1
        return hash[word]

with open('input.txt') as file:
    hash = {}
    ans = []
    nowcnt = 0
    for line in file.readlines():
        words = list(line.split())
        for word in words:
            if word not in hash:
                hash[word] = 0
            hash[word] += 1
            if hash[word] > nowcnt:
                ans = []
                ans.append(word)
                nowcnt = hash[word]
            elif hash[word] == nowcnt:
                ans.append(word)
ans = sorted(ans)
with open('output.txt', 'w') as file:
    if len(ans) == 0:
        file.write("")
    else:
        file.write(ans[0])
