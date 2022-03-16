class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        output = []
        push = 0
        pop = 0
        while push < len(pushed) or pop < len(popped):
            if len(output) != 0 and pop < len(popped) and output[-1] == popped[pop]:
                output.pop()
                pop += 1
            elif push < len(pushed):
                output.append(pushed[push])
                push += 1
            else:
                return False
        return push == len(pushed) and pop == len(popped)
