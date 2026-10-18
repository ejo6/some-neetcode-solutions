class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])

        mins = set()
        maxs = set()

        for i in range(rows):
            lucky = 100001
            for j in range(cols):
                lucky = min(lucky, matrix[i][j])
            mins.add(lucky)

        for j in range(cols):
            lucky = 0
            for i in range(rows):
                lucky = max(lucky, matrix[i][j])
            maxs.add(lucky)

        return list(mins & maxs)

