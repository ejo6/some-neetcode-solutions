class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []
        used = [False] * len(nums)

        def backtrack() -> None:
            # Base case: the permutation is full????
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                permutation.append(nums[i])
                backtrack()
                permutation.pop()
                used[i] = False
            

        backtrack()
        return result

        # Cases??? maybe should we appendleft or appent this number onto the list :/

        
