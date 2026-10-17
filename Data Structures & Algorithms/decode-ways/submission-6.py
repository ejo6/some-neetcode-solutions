class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        prev2, prev1 = 1, 1   # dp[i-2], dp[i-1]

        for i in range(2, len(s) + 1):
            curr = 0
            if s[i - 1] != '0':
                curr += prev1
            if 10 <= int(s[i - 2:i]) <= 26:
                curr += prev2
            prev2, prev1 = prev1, curr   # slide the window

        return prev1