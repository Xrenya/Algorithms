class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.task2priority = {}
        self.task2owner = {}
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap, (-priority, -taskId))
        self.task2priority[taskId] = priority
        self.task2owner[taskId] = userId
        

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.heap, (-newPriority, -taskId))
        self.task2priority[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        self.task2priority[taskId] = -1 

    def execTop(self) -> int:
        while self.heap:
            npriority, ntaskid = heapq.heappop(self.heap)
            priority = -npriority
            taskid = -ntaskid
            if self.task2priority.get(taskid, -2) == priority:
                self.task2priority[taskid] = -1
                return self.task2owner[taskid]
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
