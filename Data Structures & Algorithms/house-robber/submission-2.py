class Solution:
    def rob(self, nums: List[int]) -> int:
        # Walk through the array, and decide to rob either house i and i - 2 or i -1 1
        if len(nums) == 1: return nums[0]

        nums[1] = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        return nums[-1]
