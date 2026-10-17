class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        validIndex = n - 1

        for i in range(n - 2,-1,-1):
            # Can we jump to valid index
            if i + nums[i] >= validIndex:
                validIndex = i
        return validIndex == 0
