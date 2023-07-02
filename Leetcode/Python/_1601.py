class Solution:
    def __init__(self):
        self.ans = 0

    def max_requests(self, requests, indegree, n, index, count):
        if index == len(requests):
            for i in range(n):
                if indegree[i]:
                    return
            
            self.ans = max(self.ans, count)
            return
        
        indegree[requests[index][0]] -= 1
        indegree[requests[index][1]] += 1
        self.max_requests(requests, indegree, n, index + 1, count + 1)
        indegree[requests[index][0]] += 1
        indegree[requests[index][1]] -= 1
        self.max_requests(requests, indegree, n, index + 1, count)



    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        indegree = [0] * n
        self.max_requests(requests, indegree, n, 0, 0)
        return self.ans
