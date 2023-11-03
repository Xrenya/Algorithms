class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        idx = 0

        for i in range(1, n + 1):
            if i == target[idx]:
                output.append("Push")
                idx += 1
            else:
                output.append("Push")
                output.append("Pop")

            if idx == len(target):
                break

        return output
