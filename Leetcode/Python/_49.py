class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_dict = dict()

        for word in strs:
            key = sorted(word)
            key = "".join(key)
            if letter_dict.get(key, None) is None:
                letter_dict[key] = []
            letter_dict[key].append(word)

        return [word for word in letter_dict.values()]
