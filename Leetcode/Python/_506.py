class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        hash_order = {}
        for i, s in enumerate(sorted(score, reverse=True)):
            hash_order[s] = i
        output = []
        for n in score:
            if hash_order[n] in medals:
                output.append(medals[hash_order[n]])
            else:
                output.append(str(hash_order[n] + 1))
        return output
