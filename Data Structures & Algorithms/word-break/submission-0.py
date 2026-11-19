class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # For every word in wordDict:
        #   if it works from out curr pos:
        #       incrament our position, recurse
        #       

        # General idea: answer: if we can can get to neet, can we get to neetcode?
        #   A set of valid areas prefixes, if s[:curr + 1] in pre: return true

        # wordDict = [0, 00, 000, 1, 11]
    
        # s = 11111
        # pre = {11111} {1111, 111}
        # pre = {11111, 1111, 111} {11, 1}
        # pre = {11111, 1111, 111, 11, 1} 
        # should pre turn into curr?

        prefix = set([s])
        # print(prefix)
        curr = set()

        while len(prefix) != 0:
            for pre in prefix:
                for word in wordDict:
                    # print(f"Checking {pre} endswith {word}")
                    if pre.endswith(word):
                        newPre = pre[:len(pre) - len(word)]
                        if len(newPre) == 0: 
                            return True
                        curr.add(newPre)
                prefix = curr
            # print(prefix)
            curr = set()
        
        return False
    