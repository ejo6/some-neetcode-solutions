class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # Sort input array
        nums = sorted(nums)

        # Find triples
        candidate = 0
        while (candidate < len(nums) - 2):
            # Skip duplicates
            if candidate > 0 and nums[candidate] == nums[candidate - 1]:
                candidate += 1
                continue

            # Impossible to make 0 case
            if nums[candidate] > 0:
                break
            
            # Two pointers
            left = candidate + 1
            right = len(nums) - 1
            target = -(nums[candidate])


            while (left < right):
                sum = nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:  
                    right -= 1
                else: # sum == target
                    result.append((nums[candidate], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
            candidate += 1

        return result