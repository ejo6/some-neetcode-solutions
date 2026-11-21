class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base case (start with 0):
        pascals = [[1]]

        # Need to pascals[i][j] = pascals[i - 1][j - 1] + pascals[i - 1][j]
        for i in range(1, numRows):
            curr = []
            for j in range(i + 1):
                v1 = 0 if j - 1 < 0  else pascals[i - 1][j - 1]
                v2 = 0 if j > i - 1 else pascals[i - 1][j]

                curr.append(v1 + v2)
            pascals.append(curr)
        
        return pascals

            