# Given array of rates of employees.
# You must give each employee bonus payed.

# bonus cannot be less 500
# bonus is divisor by 500
# if rating of employee is higher then left or right empoyee in the array, then bonus should be greater
# Find minimum sum of all bonuses should be payed.

  
class Solution:
    def salary(self, ratings) -> int:
        n = len(ratings)
        min_salary = [500] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                min_salary[i] = min_salary[i - 1] + 500

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                min_salary[i] = max(min_salary[i], min_salary[i + 1] + 500)
        return sum(min_salary)
