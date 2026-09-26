class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = defaultdict(str)
        for k, v in knowledge:
            mapping[k] = v

        key = ""
        start = 0
        matching = False
        output = ""
        for i in range(len(s)):
            if s[i] == "(":
                start = i
                matching = True
            elif s[i] == ")":
                key = s[start + 1:i]
                output += mapping.get(key, "?")
                matching = False
            elif not matching:
                output += s[i]
                
        return output
