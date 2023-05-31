from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.mapping = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stationNameStart, start_t = self.check_in.pop(id)
        self.mapping[(stationNameStart, stationName)][0] += t - start_t
        self.mapping[(stationNameStart, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_trips = self.mapping[(startStation, endStation)]
        return total_time / total_trips
