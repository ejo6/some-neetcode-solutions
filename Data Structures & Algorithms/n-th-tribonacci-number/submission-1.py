class Solution:
    def tribonacci(self, n: int) -> int:
        b3, b2, b1 = 0, 1, 1
        res = 0

        if n == 0: return 0
        if n == 1 or n == 2: return 1

        for i in range(n - 2):
            res = b1 + b2 + b3
            b3, b2, b1 = b2, b1, res
        return res
