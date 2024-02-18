class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_availability = [0] * n
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            min_room_availability_time = inf
            min_available_room = 0
            found_unused_room = False
            for i in range(n):
                if room_availability[i] <= start:
                    room_availability[i] = end
                    meeting_count[i] += 1
                    found_unused_room = True
                    break
                if min_room_availability_time > room_availability[i]:
                    min_room_availability_time = room_availability[i]
                    min_available_room = i

            if not found_unused_room:
                room_availability[min_available_room] += (end - start)
                meeting_count[min_available_room] += 1
        
        return meeting_count.index(max(meeting_count))
