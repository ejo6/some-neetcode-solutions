class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []

        # Sort input array in place
        nums.sort()

        def backtrack(i: int) -> None:
            # Base case: IOB
            if i >= len(nums): 
                result.append(curr[:])
                return

            # Case 1: 
            curr.append(nums[i])
            backtrack(i + 1)

            # Case 2: Don't include and exclude duplicates
            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            curr.pop()
            backtrack(j)

        backtrack(0)
        return result