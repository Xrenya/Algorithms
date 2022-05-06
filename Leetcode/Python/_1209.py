class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        counter = []
        for c in s:
            if len(stack) == 0 or stack[-1] != c:
                stack.append(c)
                counter.append(1)
            else:
                counter[-1] += 1
            if counter[-1] == k:
                counter.pop()
                stack.pop()
                
        return ''.join([stack[i] * counter[i] for i in range(len(stack))])
