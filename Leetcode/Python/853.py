class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = []
        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)

        return len(stack)
