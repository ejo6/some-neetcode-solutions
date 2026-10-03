class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right_cols = len(matrix[0]) - 1 # m
        right_rows = len(matrix) - 1 # n

        while(left < right_rows):
            mid = (left + right_rows) // 2

            if matrix[mid][0] == target: return True
            elif matrix[mid][0] >= target: right_rows = mid - 1
            else: left = mid + 1

        if matrix[left][0] > target: row = left - 1 
        else: row = left
        left = 0


        while(left <= right_cols):
            mid = (left + right_cols) // 2

            if matrix[row][mid] == target: return True 
            elif matrix[row][mid] >= target: right_cols = mid - 1
            else: left = mid + 1

        return False




