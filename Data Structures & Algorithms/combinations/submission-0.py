class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # All possible combinations of k numbers from 1-n
        # Backtracking (no shortcuts here):
        # Num combinations: nCk? = n!/k!(n-k)!
        # We need to make include everyone of these, so 
        # Time is O(n!/k!(n-k)!)
        # Space is O(k * n!/k!(n-k)!): k elements in nCk elements

        # Imagine a list of numbers 1-n, for each combination (curr):
        #   Case 1: Include the number
        #   Case 2: Don't include the number
        #   Base case: Size of curr is k, curr to result
        #   Base case: i is larger than n 
        # return result

        # Recurse this until no calls are left

        result = [] 
        curr = []
        
        def backtrack(i: int) -> None:
            # Base case (valid combination)
            if len(curr) == k: 
                result.append(curr[:]) # needs to be a copy
                return
            # Base case (i is outside [1,n]):
            if i > n:
                return
            
            # Case 1: Include the number
            curr.append(i)
            backtrack(i + 1)

            # Case 2: Don't include the number
            curr.pop()
            backtrack(i + 1)
        
        backtrack(1)
        return result








