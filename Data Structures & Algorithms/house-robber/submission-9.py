class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,9,10,12,16]
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        if nums[0] > nums[1]: nums[1] = nums[0]
        
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        
        return nums[-1]
