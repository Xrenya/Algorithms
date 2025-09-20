class Router:

    def __init__(self, memoryLimit: int):
        self.deque = deque([])
        self.limit = memoryLimit
        self.map = {}
        # Use a deque for each destination to allow efficient O(1) removal from the front.
        self.dst = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.map:
            return False
        
        if len(self.deque) == self.limit:
            # Evict the oldest packet to make space.
            source_, destination_, timestamp_ = self.deque.popleft()
            
            # Since the oldest packet overall is being removed, it must also be the oldest
            # for its destination. This allows an O(1) pop from the front of the deque.
            if self.dst[destination_]:
                self.dst[destination_].popleft()

            self.map.pop((source_, destination_, timestamp_))

        self.map[(source, destination, timestamp)] = 1
        # Timestamps are added in increasing order, keeping the destination deques sorted.
        self.dst[destination].append((source, timestamp))
        self.deque.append((source, destination, timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if not self.deque:
            return []
        source, destination, timestamp = self.deque.popleft()
        self.map.pop((source, destination, timestamp))
        
        # The forwarded packet is the oldest, so it's at the front of the destination's deque. O(1) removal.
        if self.dst[destination]:
            self.dst[destination].popleft()

        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        packets_for_dest = self.dst[destination]
        if not packets_for_dest:
            return 0
        
        # Use binary search (bisect) for O(log K) lookup since timestamps are sorted.
        # Find the index of the first packet with timestamp >= startTime.
        start_idx = bisect.bisect_left(packets_for_dest, startTime, key=lambda x: x[1])
        
        # Find the index of the first packet with timestamp > endTime.
        end_idx = bisect.bisect_right(packets_for_dest, endTime, key=lambda x: x[1])
        
        return end_idx - start_idx


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
