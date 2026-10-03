class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
        
        for char in t:
            if char not in letters:
                return False
            else:
                letters[char] -= 1
                if letters[char] < 0: 
                    return False
                
        for value in letters.values():
            if value != 0:
                return False
        
        return True
        