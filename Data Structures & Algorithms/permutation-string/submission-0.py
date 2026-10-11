class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Quick base case
        if len(s2) < len(s1): return False

        left, right = 0, len(s1)
        
        # Slide the window down
        freq = [0] * 26
        for c in s1: freq[ord(c) - ord('a')] += 1

        # 
        i = 0 
        while i < len(s1):
            freq[ord(s2[i]) - ord('a')] -= 1
            i += 1

        print(freq)

        # Check if the first len(s1) chars of s2 is a valid permutation
        for j in range(26): 
            if freq[j] != 0: break
            if j == 25: return True

        while right < len(s2):
            print(freq)
            freq[ord(s2[right]) - ord('a')] -= 1
            right += 1
            freq[ord(s2[left]) - ord('a')] += 1
            left += 1

            for j in range(26): 
                if freq[j] != 0: break
                if j == 25: return True

        return False
            
        



    
       