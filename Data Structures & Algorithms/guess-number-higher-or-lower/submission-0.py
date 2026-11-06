# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # bounds are between 1 and n
        # call guess(mid), run a binary search each time

        l, h = 1, n

        while l <= h:
            mid = l + (h - l) // 2
            res = guess(mid)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                h = mid - 1
            elif guess(mid) == 1:
                l = mid + 1
        return -1 
            
    


        
        