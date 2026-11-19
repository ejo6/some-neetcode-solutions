class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        
        squares = []

        i = 1
        while i ** 2 <= n:
            squares.append(i ** 2)
            i += 1

        for square in squares:
            for j in range(square, n + 1):
                dp[j] = min(dp[j - square] + 1, dp[j])
        
        # print(dp)
        return dp[-1]

        # [0, i, i, i, i, i, i]
        # [1, 4]
        # [0, 1, 2, 3, 1, 2, 3]

        
