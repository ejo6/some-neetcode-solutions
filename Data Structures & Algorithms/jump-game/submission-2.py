class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0: 
            return True
        
        nums[-1] = -1

        for i in range(len(nums) - 2,-1,-1):
            if nums[i] == 0: 
                continue

            # Check if we can reach a valid index
            for j in range(1,nums[i] + 1):
                if i + j < len(nums) and nums[i + j] == -1:
                    nums[i] = -1

        return nums[0] == -1


