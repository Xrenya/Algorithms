class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for char in tasks:
            freq[ord(char) - ord('A')] += 1

        pq = [-value for value in freq if value > 0]
        heapq.heapify(pq)

        time = 0
        while pq:
            cycle = n + 1
            store = []
            tasks_count = 0
            while cycle > 0 and pq:
                cur_freq = -heapq.heappop(pq)
                if cur_freq > 1:
                    store.append(-(cur_freq - 1))

                tasks_count += 1
                cycle -= 1

            for x in store:
                heapq.heappush(pq, x)
            time += tasks_count if not pq else n + 1

        return time
