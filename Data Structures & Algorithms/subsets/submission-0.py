class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(start: int):
            if start >= len(nums):
                result.append(subset[:]) # copy
                return

            subset.append(nums[start])
            backtrack(start + 1)
        
            subset.pop()
            backtrack(start + 1)

        backtrack(0)
        return result

    # [[], [1], [1,2], [1, 2, 3]]
    # [1, 2, 3]