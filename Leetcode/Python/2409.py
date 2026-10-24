class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def calc(day):
            month = int(day[:2])
            date = int(day[3:])
            return prefix[month - 1] + date
        
        dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = [0]
        for date in dates:
            prefix.append(prefix[-1] + date)

        arriveAliceDay = calc(arriveAlice)
        leaveAliceDay = calc(leaveAlice)
        arriveBobDay = calc(arriveBob)
        leaveBobDay = calc(leaveBob)
        return max(
            0,
            min(leaveAliceDay, leaveBobDay)
            - max(arriveAliceDay, arriveBobDay)
            + 1,
        )
