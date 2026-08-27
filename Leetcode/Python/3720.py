class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        if len(s) != len(target):
            return ""

        count = Counter(s)
        prefix = []


        def smallest_greatest(char):
            for c in sorted(count):
                if count[c] > 0 and c > char:
                    return c
            return None

        def build_answer(prefix, chosen):
            count[chosen] -= 1
            suffix = []
            for c in sorted(count):
                suffix.append(c * count[c])

            return "".join(prefix) + chosen + "".join(suffix)

        for i, char in enumerate(target):
            if count[char] > 0:
                count[char] -= 1
                prefix.append(char)
            else:
                bigger = smallest_greatest(char)
                if bigger is not None:
                    return build_answer(prefix, bigger)

                break

        for pos in range(len(prefix) - 1, -1, -1):
            used = prefix.pop()
            count[used] += 1

            bigger = smallest_greatest(target[pos])
            if bigger is not None:
                    return build_answer(prefix, bigger)
        return ""
