class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Maximum number of fruits we can pick
        max_picked = 0
        left = 0
        n = len(fruits)
        basket = {}
        for right in range(n):
            add_fruit = fruits[right]
            if add_fruit not in basket:
                basket[add_fruit] = 0
            basket[add_fruit] += 1
            while len(basket) == 3:
                remove_fruit = fruits[left]
                basket[remove_fruit] -= 1
                if basket[remove_fruit] == 0:
                    del basket[remove_fruit]
                left += 1
            max_picked = max(max_picked, sum(basket.values()))

        return max_picked
    
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
