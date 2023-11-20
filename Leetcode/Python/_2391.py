class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix = [0] * (len(travel) + 1)
        prefix[1] = travel[0]
        for i in range(1, len(travel)):
            prefix[i + 1] = prefix[i] + travel[i]

        print(prefix)
        garbage_last_pos = {}
        garbage_count = {}

        for i, g in enumerate(garbage):
            for t in g:
                garbage_last_pos[t] = i
                garbage_count[t] = garbage_count.get(t, 0) + 1

        output = 0
        for t in ["G", "P", "M"]:
            if garbage_count.get(t, 0):
                output += prefix[garbage_last_pos[t]] + garbage_count[t]

        return output
