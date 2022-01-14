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
