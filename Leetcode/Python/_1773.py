class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # Time complexity O(n)
        # Iterate over the list and check matches
        matches = 0
        rule = {"type": 0, "color": 1, "name": 2}
        for item in items:
            if item[rule[ruleKey]] == ruleValue:
                matches += 1
        return matches
