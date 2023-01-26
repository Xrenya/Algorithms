class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        total = len(rooms)
        visited = set()
        visited.add(0)
        queue = deque()
        for r in rooms[0]:
            queue.append(r)
        while queue:
            key = queue.popleft()
            if key not in visited:
                visited.add(key)
                for room in rooms[key]:
                    queue.append(room)

        return len(visited) == total
