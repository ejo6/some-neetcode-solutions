class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i: int) -> None:
            # Base case (we are pas the last index):
            if i >= len(nums):
                result.append(subset[:]) # remember to copy
                return

            # Branch 1: (include the current number)
            subset.append(nums[i])
            backtrack(i + 1)

            # Branch 2: (don't include the current number)
            subset.pop()
            backtrack(i + 1)

        backtrack(0)   
        return result
