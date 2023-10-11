class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        sorted_people = sorted(people)
        mapping = {}
        heap = []
        
        i = 0
        for p in sorted_people:
            while i < len(flowers) and flowers[i][0] <= p:
                heapq.heappush(heap, flowers[i][1])
                i += 1
                
            while heap and heap[0] < p:
                heapq.heappop(heap)
                
            mapping[p] = len(heap)
        
        return [mapping[k] for k in people]
