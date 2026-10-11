class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        curr = []

        def backtrack(i: int, total: int) -> None:
            # Base case 1: total is the target
            if total == target: 
                result.append(curr[:])
                return

            # Base case 2: Out of bounds
            if i >= len(candidates) or total > target:
                return

            # Case 1: Include the current candidates[i]
            curr.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            
            # Case 2: Exclude of candidates[i] and duplicates
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            curr.pop()
            backtrack(j, total)
            
        backtrack(0, 0)
        return result