class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def to_dict(s):
            hashmap = {}
            for c in s:
                if c not in hashmap:
                    hashmap[c] = 0
                hashmap[c] += 1
                
            return hashmap
        
        p_dict = to_dict(p)
        
        output = []
        for i in range(0, len(s) - len(p) + 1, 1):
            if i != 0:
                remove_char = s[i - 1]
                add_char = s[i + len(p) - 1]
                if temp[remove_char] - 1 == 0:
                    del temp[remove_char]
                else:
                    temp[remove_char] -= 1
                if add_char not in temp:
                    temp[add_char] = 1
                else:
                    temp[add_char] += 1
            else:
                temp = to_dict(s[i:i + len(p)])
                
            if temp == p_dict:
                output.append(i)
                
        return output
