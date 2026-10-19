class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Total number of ones (aka window size)
        numOnes = 0
        for num in nums: 
            if num == 1: numOnes += 1

        if numOnes < 2: 
            return 0

        l, r, = 0, numOnes - 1
        best = float('inf')
        
        onesIn = 0
        for i in range(numOnes):
            if nums[i] == 1: onesIn += 1

        # 
        while l < len(nums):
            best = min(best, numOnes - onesIn)

            l += 1; r += 1
            if r == len(nums):
                r = 0

            onesIn -= nums[l - 1]
            onesIn += nums[r]

        return best

        # [|1, 0, 0, 1|, 0, 1, 1, 0, 0]
        # 1s: 4
        # 1s in: 1
        # 0s in: 3 (windowSize - 1s in), also the number of swaps

        # Once we get to the end, slide window around