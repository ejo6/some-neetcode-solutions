class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        best = nums[0]

        for i in range(1,len(nums)):
            # Not helpful
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]  
            best = max(nums[i], best)     
     
        return best

        # [2,-1,4,2,4,5,4,8]