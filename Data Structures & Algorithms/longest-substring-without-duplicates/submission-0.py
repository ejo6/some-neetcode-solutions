class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        cur = 0
        slow = 0
        fast = 0
        seen = set()

        while fast < len(s):
            if s[fast] in seen:
                # shrink window until we remove previous occurrence of s[fast]
                while s[slow] != s[fast]:
                    seen.remove(s[slow])
                    slow += 1
                # also drop the previous occurrence itself
                seen.remove(s[slow])
                slow += 1
            else:
                seen.add(s[fast])
                cur = fast - slow + 1
                longest = max(longest, cur)
                fast += 1
        return longest