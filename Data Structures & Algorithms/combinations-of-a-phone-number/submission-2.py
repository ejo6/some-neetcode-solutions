class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        result = []
        curr = ""

        mappings = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }

        def backtrack(i: int) -> None:
            nonlocal curr

            # Base case: we've reached the end of digits
            if i == len(digits):
                if len(curr) == len(digits):
                    result.append(curr[:])
                return
            
            for j in range(len(mappings[digits[i]])):
                curr += mappings[digits[i]][j]
                backtrack(i + 1)
                curr = curr[:-1]


        backtrack(0)
        return result