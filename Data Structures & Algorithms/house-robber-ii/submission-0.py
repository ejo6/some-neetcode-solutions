class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def linearRob(nums: List[int]):
            prev1, prev2 = 0, 0
            for n in nums:
                best = max(prev1, n + prev2)
                prev2 = prev1
                prev1 = best
            
            return prev1
        
        return max(linearRob(nums[1:]), linearRob(nums[:-1]))

            
    

