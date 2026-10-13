class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        greatest = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = greatest
            greatest = max(temp, greatest)

        return arr
        # [,2,2,-1]
        # greatest = 3
        # temp = 3
