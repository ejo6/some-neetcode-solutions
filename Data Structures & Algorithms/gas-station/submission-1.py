class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 

        gasLeft = 0
        start = 0

        for i in range(len(gas)):
            gasLeft += (gas[i] - cost[i])
            if gasLeft < 0:
                gasLeft = 0
                start = i + 1
        
        return start

                



            
