class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def to_dict(string):
            hash_map = {}
            for s in string:
                hash_map[s] = hash_map.get(s, 0) + 1
                
            return hash_map
        
        r = to_dict(ransomNote)
        m = to_dict(magazine)
        
        for c in ransomNote:
            if r[c] > m.get(c, 0):
                return False
            
        return True
