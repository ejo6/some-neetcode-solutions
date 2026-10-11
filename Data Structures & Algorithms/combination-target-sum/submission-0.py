class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []

        def backtrack(i: int, total: int):
            # Base cases:
            if total == target:
                result.append(curr[:])
                return
            if i >= len(nums) or total > target:
                return 

            # Case 1: include the current number
            curr.append(nums[i])
            backtrack(i, total + nums[i])

            # Case 2: don't include the current number
            curr.pop()
            backtrack(i + 1, total)

        backtrack(0, 0)
        return result

