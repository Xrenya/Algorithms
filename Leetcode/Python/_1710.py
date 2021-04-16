class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        acc = 0
        for num, unit in boxTypes:
            if num<truckSize:
                size = num
            else:
                size = truckSize
            acc += size * unit
            truckSize -= size
            if truckSize == 0:
                break
        return acc
      
      
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = [[-u, -b] for b, u in boxTypes]
        print(heap)
        heapify(heap)
        units = 0
        while heap:
            u, b = heappop(heap)
            if -b > truckSize:
                return units - truckSize * u
            units += u * b
            truckSize += b
        return units
