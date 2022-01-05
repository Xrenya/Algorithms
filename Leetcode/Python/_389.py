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
