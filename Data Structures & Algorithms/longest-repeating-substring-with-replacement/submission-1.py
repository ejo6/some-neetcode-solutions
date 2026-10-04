class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowFreqeuncy = defaultdict(int)
        slow = 0 
        fast = 0
        maxFreq = 0
        best = 0

        while (fast < len(s)):
            windowFreqeuncy[s[fast]] += 1
            maxFreq = max(maxFreq, windowFreqeuncy[s[fast]])

            if (((fast + 1 - slow ) - maxFreq) <= k):
                best = fast - slow + 1
            else: 
                windowFreqeuncy[s[slow]] -= 1
                slow += 1
            
            fast += 1
        return best


"""
charReplacement(s: string, k: int) returns int:
    window_frequency = dict(int:int)




"""