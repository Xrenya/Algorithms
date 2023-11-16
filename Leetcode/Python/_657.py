class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1
            else:
                x += 1
        return x == 0 and y == 0


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        starting_point = [0, 0]
        hashMap = {"R": [1, 0], "L": [-1, 0],
                   "U": [0, 1], "D": [0, -1]}
        for move in moves:
            starting_point[0] += hashMap[move][0]
            starting_point[1] += hashMap[move][1]
        return starting_point == [0, 0]


class Solution:
    def judgeCircle(self, m: str) -> bool:
        hashMap = {"R": 0, "L": 0,
                   "U": 0, "D": 0}
        for move in m:
            hashMap[move] += 1
        if hashMap["R"]==hashMap["L"] and hashMap["U"]==hashMap["D"]:
            return True
        return False


class Solution:
    def judgeCircle(self, m: str) -> bool:
        hashMap = {"R": 0, "L": 0,
                   "U": 0, "D": 0}
        for move in m:
            hashMap[move] += 1
        return hashMap["R"]==hashMap["L"] and hashMap["U"]==hashMap["D"]
      
class Solution:
    def judgeCircle(self, m: str) -> bool:
        return m.count("D") == m.count("U") and m.count("R") == m.count("L")
