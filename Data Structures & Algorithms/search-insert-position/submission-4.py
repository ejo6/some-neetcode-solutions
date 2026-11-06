# import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Search on target, keep track of the best index so far (closest less than target)
        # If we find the target, short circuit and return it, else:
        #     return the bestIndexSoFar + 1
        # Need to handle 0th index insert

        # Could just use a bisect:
        # return bisect.bisect_left(nums, target)

        l, h = 0, len(nums) - 1
        res = -1

        while l <= h:
            mid = (l + h) // 2 # our index
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target:
                res = mid
                l = mid + 1
            elif nums[mid] > target:
                h = mid - 1
        return res + 1


                

            

