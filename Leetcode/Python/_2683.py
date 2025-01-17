class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original = [0]
        for i in range(len(derived)):
            original.append(derived[i] ^ original[i])

        check_zero = original[0] == original[-1]
        original = [1]
        for i in range(len(derived)):
            original.append(derived[i] ^ original[i])
        check_one = original[0] == original[-1]

        return check_zero or check_one
