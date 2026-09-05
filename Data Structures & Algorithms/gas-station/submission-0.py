class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        curr_tank = 0
        total_tank = 0
        start_candidate = 0

        for i in range(n):
            total_tank = total_tank + gas[i] - cost[i]
            curr_tank = curr_tank + gas[i] - cost[i]
            if curr_tank < 0:
                curr_tank = 0
                start_candidate = i + 1

        return start_candidate if total_tank >= 0 else -1