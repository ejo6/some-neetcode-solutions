class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []

        def backtrack(i: int, total: int) -> None:
            # Base case 1: we are outside the bounds of nums
            if i >= len(nums) or total > target:
                return
            # Base case 2: we found a sum
            if total == target: 
                result.append(curr[:])
                return

            # Branch 1: include the current number
            curr.append(nums[i])
            backtrack(i, total + nums[i]) # don't incrament i, we can use the same i twice

            # Branch 2: don't include the current number
            curr.pop()
            backtrack(i + 1, total) # do incrament i, go to the next number

        backtrack(0, 0)
        return result
