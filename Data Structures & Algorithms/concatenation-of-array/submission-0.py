class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Literally just append an array
        # This is going to be O(n) time
        # Should NOT copy and append the array, that's extra space
        # Python: modify nums, so we don't create a new object, this would
        # need some verification IRL

        l = len(nums)
        for i in range(l):
            nums.append(nums[i])
        
        return nums

