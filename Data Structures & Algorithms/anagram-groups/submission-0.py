class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            letters = [0] * 26
            for char in word:
                letters[ord(char) - ord("a")] += 1
            anagrams[tuple(letters)].append(word) # lists cannot be keys in python

        return list(anagrams.values())


                 