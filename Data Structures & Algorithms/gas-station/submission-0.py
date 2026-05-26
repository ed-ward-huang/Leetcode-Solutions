class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        currentGas = 0
        startingIndex = 0
        for i in range(len(gas)):
            if currentGas < 0:
                startingIndex = i
                currentGas = 0
            currentGas += (gas[i] - cost[i])
        
        return startingIndex
        

