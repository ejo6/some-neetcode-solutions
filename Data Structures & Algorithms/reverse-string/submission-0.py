class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Need to modify s in place
        # alg:
        #   pointer on each end, incrament left and decrament right while left < right (strictly)
        #   swap the two values at each pointer, need to store a temp
        #   O(n) time, O(1) space

        l, r = 0, len(s) - 1
        while l < r:
            t = s[l]
            s[l] = s[r]
            s[r] = t
            l += 1; r -= 1

        