class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        deletions = 0
        used_freq = set()

        heap = list(count.values())
        heapq.heapify(heap)

        while heap:
            freq = heapq.heappop(heap)
            while freq > 0 and freq in used_freq:
                freq -= 1
                deletions += 1
            used_freq.add(freq)
        return deletions


class Solution:
    def minDeletions(self, s: str) -> int:
        hashmap = defaultdict(int)
        myset = set()
        for c in s:
            hashmap[c] += 1
        deletion = 0
        for val in sorted(hashmap.values(), reverse=True):
            if val not in myset:
                myset.add(val)
            else:
                cur = val
                while True:
                    if cur == 0 or cur not in myset:
                        break
                    cur -= 1
                    deletion += 1
                myset.add(cur)
        return deletion
