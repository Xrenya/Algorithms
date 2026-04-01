class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        output = []
        stack = deque()

        indices.sort(key=lambda x: positions[x])

        for cur_idx in indices:
            if directions[cur_idx] == "R":
                stack.append(cur_idx)
            else:
                while stack and healths[cur_idx] > 0:
                    top_idx = stack.pop()
                    if healths[top_idx] > healths[cur_idx]:
                        healths[top_idx] -= 1
                        healths[cur_idx] = 0
                        stack.append(top_idx)
                    elif healths[top_idx] < healths[cur_idx]:
                        healths[cur_idx] -= 1
                        healths[top_idx] = 0
                    else:
                        healths[cur_idx] = 0
                        healths[top_idx] = 0

        for idx in range(n):
            if healths[idx] > 0:
                output.append(healths[idx])

        return output
