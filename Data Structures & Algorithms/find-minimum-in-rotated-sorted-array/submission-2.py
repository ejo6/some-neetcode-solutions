class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1   # min is strictly to the right of mid
            else:
                right = mid      # mid could be the min, keep it

        return nums[left]

        # 5 

