class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Go get all numbers:
            j = i
            while s[j] != '#':
                j += 1
            word_length = int(s[i:j])
            word = s[j + 1:j + word_length + 1]
            result.append(word)
            i = word_length + j + 1
            print(result)
        return result
