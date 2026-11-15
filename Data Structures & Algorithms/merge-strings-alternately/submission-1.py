class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Super trivial, want to do this in the cleanest way
        # O(n + m) time, len(word1) = n, len(word2) = m
        # Do we need auxillary space?
        #   Yes, inserting inplace into word1 will create m * O(n) or n * O(m) inserts
        #   And we would need some auxillary storage to start remembering things
        #   At this point, use an auxillary unless we have significantly constrained memory
        #   IMPORTANT: In python, we need to append to a list, and join at the end
        # O(n + m) space

        l = min(len(word1), len(word2))
        res = []
        for i in range(l):
            res.append(word1[i] + word2[i])
        res.append(word1[l:] + word2[l:])
        return "".join(res)