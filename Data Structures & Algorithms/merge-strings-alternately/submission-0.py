class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Super trivial, want to do this in the cleanest way
        # O(n + m) time, len(word1) = n, len(word2) = m
        # Do we need auxillary space?
        #   Yes, inserting inplace into word1 will create m * O(n) or n * O(m) inserts
        #   And we would need some auxillary storage to start remembering things
        #   At this point, use an auxillary unless we have significantly constrained memory
        #   IMPORTANT: In python, we need to append to a list, and join at the end

        l = min(len(word1), len(word2))
        res = []
        for i in range(l):
            res.append(word1[i])
            res.append(word2[i])
        
        # This may be empty, or the rest
        res.append(word1[l:len(word1)])
        res.append(word2[l:len(word2)])

        return "".join(res)