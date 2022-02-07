class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def to_dict(s):
            hash_map = defaultdict(int)
            for c in s:
                hash_map[c] += 1
            return hash_map
        
        s_counter = to_dict(s)
        t_counter = to_dict(t)
        
        for key, val in t_counter.items():
            if val - s_counter.get(key, 0) == 1:
                return key

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def to_hash(s):
            hash_dict = {}
            for c in s:
                if c not in hash_dict:
                    hash_dict[c] = 0
                hash_dict[c] += 1
            return hash_dict
        
        s_dict = to_hash(s)
        for c in t:
            if c not in s_dict:
                return c
            s_dict[c] -= 1
            if s_dict[c] == 0:
                s_dict.pop(c)
        return s_dict.key()
                
            
