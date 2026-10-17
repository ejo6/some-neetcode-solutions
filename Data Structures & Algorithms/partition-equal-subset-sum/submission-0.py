class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        dp = {0}

        for n in nums:
            curr = set(dp) # need to copy
            for total in dp:
                curr.add(n + total)
            dp = curr

        print(dp)

        return (sum(nums) // 2) in dp
