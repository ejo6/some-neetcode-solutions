class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost = [1,2,1,2,1,1,1,0]
        # p2 2
        # p1 2

        p1, p2 = 0, 0
        cost.append(0)

        for i in range(2, len(cost)):
            tmp = p1
            p1 = min(p1 + cost[i - 1], p2 + cost[i - 2])
            p2 = tmp

        return p1

