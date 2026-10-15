class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        curr = []

        def isPalindrome(st: str):
            l, r = 0, len(st) - 1
            while l < r:
                if st[l] != st[r]: return False
                l += 1
                r -= 1
            return True

        def backtrack(start: int):
            if start == len(s):
                result.append(curr[:])
                return

            for end in range(start, len(s)):
                piece = s[start:end + 1]
                if isPalindrome(piece):
                    curr.append(piece)
                    backtrack(end + 1)
                    curr.pop()

        backtrack(0)
        return result

        