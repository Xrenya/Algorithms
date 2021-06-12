def two_sum(array, target):
    prevnum = set()
    for nownum in array:
        if target - nownum in prevnum:
            return nownum, target - nownum 
        prevnum.add(nownum)
    return 0, 0

def groupword(words):
    groups = {}
    for word in words:
        sortedword = "".join(sorted(word)) # not good solution in case of long word
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
    assert groupword(["eat", "ate", "two", "wto", "otw"]) == [['eat', 'ate'], ['two', 'wto', 'otw']]
    return ans

def groupword(words):
    def keywords(word):
        syncnt = {}
        for sym in word:
            if sym not in syncnt:
                syncnt[sym] = 0
            syncnt[sym] += 1
        lst = []
        for sym in sorted(syncnt.keys()):
            lst.append(sym)
            lst.append(str(syncnt[sym]))
        return "".join(lst) # Question: in which case it is possible to break this function?

    groups = {}
    for word in words:
        sortedword = keywords(word)
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
    return ans
