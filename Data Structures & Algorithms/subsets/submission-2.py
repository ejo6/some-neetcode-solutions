class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []

        def backtrack(i: int) -> None:
            # Base case: IOB
            if i >= len(nums):
                result.append(curr[:]) # (copying) 
                return

            # Case 1: Include the current nums[i]
            curr.append(nums[i])
            backtrack(i + 1)

            # Case 2: Don't include the current nums[i]
            curr.pop()
            backtrack(i + 1)

        backtrack(0)
        return result
