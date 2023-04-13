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

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) < len(popped):
            return False

        total_len = len(pushed)
        index, pop_index = 0, 0
        array = []
        while index < total_len:
            if array and array[-1] == popped[pop_index]:
                pop_index += 1
                array.pop()
            else:
              array.append(pushed[index])
              index += 1
            
        while array or pop_index < len(popped):
            if array[-1] == popped[pop_index]:
                pop_index += 1
                array.pop()
            else:
              break
        return len(array) == 0 and pop_index == len(popped)
