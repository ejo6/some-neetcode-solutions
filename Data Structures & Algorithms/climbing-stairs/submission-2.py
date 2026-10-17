class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1

        # dp[i] = dp[i - 1] + dp[i - 2]
        prev2, prev1 = 1, 1

        for i in range(0, n - 1):
            tmp = prev1
            prev1 += prev2
            prev2 = tmp
        
        return prev1

        # [1, 1, 2, 3