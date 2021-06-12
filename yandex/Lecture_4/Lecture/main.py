def isdigitpermutation(x, y):
    def countdigits(num):
        digitcount = [0] * 10
        while num > 0:
            lastdigit = num % 10
            digitcount[lastdigit] += 1
            num //= 10
        return digitcount

    digitsx = countdigits(x)
    digitsy = countdigits(y)
    for digit in range(10):
        if digitsx[digit] != digitsy[digit]:
            return False
    return True 

def isdigitpermutation_hash(x, y):
    def countdigits(num):
        digitcount = {}
        while num > 0:
            lastdigit = num % 10
            if lastdigit not in digitcount:
                digitcount[lastdigit] = 0
            digitcount[lastdigit] += 1
            num //= 10
        return digitcount

    digitsx = countdigits(x)
    digitsy = countdigits(y)
    for digit in range(10):
        if digitsx.get(digit, 0) != digitsy.get(digit, 0):
            return False
    return True 

def countbeatrooks(rookcoords):
    def addrook(roworcol, key):
        if key not in roworcol:
            roworcol[key] = 0
        roworcol[key] += 1
    
    def countpairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] - 1
        return pairs

    rooksinrow = {}
    rooksincol = {}
    for row, col in rookcoords:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)
        print(rooksinrow, rooksincol)
    return countpairs(rooksinrow) + countpairs(rooksincol)

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
