class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []

        def backtrack(index: int, total: int):
            # Base case: we've summed to target
            if total == target:
                result.append(curr[:])
                return
            # Base case: we've no more numbers to try (OOB) or exceeded target
            if index >= len(nums) or total > target:
                return

            # Case 1: Include the current number:
            curr.append(nums[index])
            backtrack(index, total + nums[index])

            # Case 2: Don't Include the current number
            curr.pop()
            backtrack(index + 1, total)

        backtrack(0, 0)
        return result