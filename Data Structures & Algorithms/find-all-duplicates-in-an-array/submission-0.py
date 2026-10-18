class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            curr = abs(nums[i])
            if nums[curr - 1] < 0:
                res.append(curr)
                continue
            nums[curr - 1] = -(nums[curr - 1])
            
        return res
        # [-3, -1, -3, 2, 2]