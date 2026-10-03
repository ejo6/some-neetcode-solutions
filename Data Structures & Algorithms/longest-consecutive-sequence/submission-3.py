class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = {}
        best = 0

        for num in nums:
            if num in vals:
                continue  # ignore duplicates

            left = vals.get(num - 1, 0)
            right = vals.get(num + 1, 0)
            cur = left + 1 + right

            vals[num] = cur
            vals[num - left] = cur   # left bound
            vals[num + right] = cur  # right bound

            if cur > best:
                best = cur

        return best