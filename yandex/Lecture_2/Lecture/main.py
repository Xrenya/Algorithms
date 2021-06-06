def find_left_x(seq, x):
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans

def find_right_x(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans

def find_max(seq):
    ans = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > ans:
            ans = seq[i]
    return ans

def find_max_indexing(seq):
    # save space since you do not copy the 
    # seq but it takes since you are refering to index
    ans = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > ans:
            ans = i
    return seq[ans]

def find_max_and_prev(seq):
    now_max = max(seq[:2])
    prev = min(seq[:2])
    for i in range(2, len(seq)):
        if seq[i] > now_max:
            prev = now_max
            now_max = seq[i]
        elif seq[i] > prev:
            prev = seq[i]
    return prev, now_max

def find_min(seq):
    ans = -1
    flag = False
    for i in range(len(seq)):
        if seq[i] % 2 != 0 and (not flag or 
                                seq[i] < min_now):
            ans = seq[i]
            flag = True
    return ans

def shortwords(words):
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(word)
    ans = []
    # if ans = "" -> elements would copy all time
    # so array would take O(1)
    for word in words:
        if len(word) == minlen:
            ans.append(word)
    return " ".join(ans)
