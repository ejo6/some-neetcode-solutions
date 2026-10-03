class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        zero_present = False
        zero_index = 0

        # Compute the total
        total = 1
        for i in range(len(nums)):
            if nums[i] == 0 and not zero_present: # case of 1 zero
                zero_present = True
                zero_index = i
            elif nums[i] == 0 and zero_present: # case of 2 zeros
                return self.setToZero(len(nums))
            else:
                total *= nums[i]
            
        # Fill in the lists
        if not zero_present:
            for num in nums:
                res = total // num
                result.append(res)
        else:
            for i in range(len(nums)):
                if i != zero_index:
                    result.append(0)
                else:
                    res = total
                    result.append(res)

        return result

    def setToZero(self, length: int) -> List[int]:
        result = []
        for i in range(length):
            result.append(0)
        return result




