from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
      #0.edge cases
      if start == end: 
          return True
      visited = set()
      queue = deque()
      queue.append(start)


      while queue:
          node = queue.popleft()
          for neighbor in adj[node]:
              if neighbor not in visited:
                  if neighbor == end:
                      return True
                  else:
                      queue.append(neighbor)
          visited.add(node)
      return False
