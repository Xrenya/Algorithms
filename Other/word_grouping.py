# Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
#
# Т.е. сгруппировать слова по "общим буквам".
sample = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_words(words):
    letter_dict = dict()

    for word in words:
        key = sorted(word)
        key = "".join(key)
        if letter_dict.get(key, None) is None:
            letter_dict[key] = []
        letter_dict[key].append(word)

    return sorted([word for word in letter_dict.values()])

print(group_words(sample))

def get_hash(s):
    count = [0]*26
    for c in s:
        count[ord(c) - ord('a')] += 1
    return "".join(map(str, count))

def hash_group_words(words):
    letter_dict = dict()

    for word in words:
        hash = get_hash(word)
        if hash not in letter_dict:
            letter_dict[hash] = []
        letter_dict[hash].append(word)

    return sorted([word for word in letter_dict.values()])

print(hash_group_words(sample))


            
