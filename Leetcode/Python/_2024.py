class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_len = k
        count = Counter(answerKey[:k])

        left = 0
        for right in range(k, len(answerKey)):
            count[answerKey[right]] += 1

            while min(count["T"], count["F"]) > k:
                count[answerKey[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left, right = k, n
        def is_valid(size):
            counter = Counter(answerKey[:size])
            if min(counter['T'], counter['F']) <= k:
                return True
            for i in range(size, n):
                counter[answerKey[i]] += 1
                counter[answerKey[i - size]] -= 1
                if min(counter['T'], counter['F']) <= k:
                    return True
            return False
        
        while left < right:
            m = left + (right - left + 1) // 2
            
            if is_valid(m):
                left = m
            else:
                right = m - 1

        return left
