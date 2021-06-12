n = int(input())
hash = {}
languages = []
for i in range(n):
    hash[i] = []
    for j in range(int(input())):
        lng = str(input())
        hash[i].append(lng)
        if lng not in languages:
            languages.append(lng)

def poly(hash, languages):
    know = set(languages.copy())
    for value in hash.values():
        know &= set(value)
    print(len(know))
    for lan in know:
        print(lan)

    print(len(languages))
    for lan in languages:
        print(lan)
    


poly(hash, languages)
