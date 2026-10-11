class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        curr = []
        
        def backtrack(openCount: int, closeCount: int) -> None:
            # Base case: our parentheses string is too long
            if len(curr) == 2 * n:
                # We can ONLY get here if open and close counts are equal
                # We always appened the ( first, then if it was valid: append )
                # This base case represents a valid parentheses
                # Key insight here is that the string needed to be validated BEFORE recursing on it
                # Otherwise that's just a brute force call. Not helpful
                result.append(''.join(curr))
                return

            # Case 1: append the '('
            if openCount < n:
                curr.append('(')
                backtrack(openCount + 1, closeCount)
                curr.pop()

            # Case 1: append the ')'
            if closeCount < openCount:
                curr.append(')')
                backtrack(openCount, closeCount + 1)
                curr.pop()

        backtrack(0,0)
        return result
            



        
