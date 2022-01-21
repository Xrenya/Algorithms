class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_pos = 0
        surplus = 0
        deficit = 0
        for i in range(len(gas)):
            surplus += gas[i] - cost[i]
            if surplus < 0:
                start_pos = i + 1
                deficit += surplus
                surplus = 0
        return start_pos if surplus + deficit >= 0 else -1
