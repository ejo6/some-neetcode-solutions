class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True:
            # Current candidate character
            if i >= len(strs[0]):
                return s[0:i] if i > 0 else ""
            c = strs[0][i]                     

            for s in strs:
                # If we broke the prefix or OOB
                if i >= len(s) or s[i] != c:
                    return s[0:i] if i > 0 else ""
            i += 1
        
            