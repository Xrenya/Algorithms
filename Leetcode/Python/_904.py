class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        s = fruits
        k = 2
        counter = dict()
        maximum = 0
        left = 0
        for right in range(len(s)):
            right_char = s[right]
            counter[right_char] = counter.get(right_char, 0) + 1
            while len(counter) > k:
                left_char = s[left]
                counter[left_char] -= 1
                if counter[left_char] == 0:
                    del counter[left_char]
                left += 1
            maximum = max(maximum, right - left + 1)


        return maximum
