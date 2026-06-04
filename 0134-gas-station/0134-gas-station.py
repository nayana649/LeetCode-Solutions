class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # Insight 1: If total fuel is less than total consumption, no solution exists
        if sum(gas) < sum(cost):
            return -1
            
        start_index = 0
        current_tank = 0
        
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            
            # Insight 2: If we run dry, station 'i' or any prior station cannot be the start
            if current_tank < 0:
                # Reset tank and attempt starting from the next station
                start_index = i + 1
                current_tank = 0
                
        return start_index