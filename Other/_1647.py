class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        deletions = 0
        used_freq = set()

        heap = list(count.values())
        heapq.heapify(heap)

        while heap:
            print(heap)
            freq = heapq.heappop(heap)
            while freq > 0 and freq in used_freq:
                freq -= 1
                deletions += 1
            used_freq.add(freq)
        return deletions
