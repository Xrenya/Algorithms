class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_id = 0
        s_id = 0
        while g_id < len(g) and s_id < len(s):
            if s[s_id] >= g[g_id]:
                g_id += 1
            s_id += 1
        return g_id
