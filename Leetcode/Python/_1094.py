class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        event = []
        for i in range(len(trips)):
            nums, from_ , to_ = trips[i]
            event.append([from_, nums])
            event.append([to_, -nums])
        event.sort()
        cnt = 0
        for i in range(len(event)):
            cnt += event[i][1]
            if cnt > capacity:
                return False
        return True
