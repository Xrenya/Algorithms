class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Iterate over the customer and sum values into temp and compare with summ, which is the highest value
        # if it less than temp, assign summ a new temp value
        # Time complexity O(m*n)
        summ = 0
        temp = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                temp += accounts[i][j]
            if temp > summ:
                summ = temp
            temp = 0
        return summ
