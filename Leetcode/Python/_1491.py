class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = +inf
        maximum = -inf
        acc = 0
        for num in salary:
            if minimum > num:
                minimum = num
            if maximum < num:
                maximum = num
            acc += num
        return (acc - minimum - maximum) / (len(salary) - 2)
        
class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
