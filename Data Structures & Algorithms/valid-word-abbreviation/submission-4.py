class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # A pointer on each word:
        a = 0
        w = 0

        while a < len(abbr) and w < len(word):
            # If we're on a letter:
            if (not abbr[a].isdigit()):
                if abbr[a] != word[w]:
                    return False
                a += 1
                w += 1
                continue

            # 
            if abbr[a] == '0':
                return False

            # If we're abreviating:
            num = 0
            while a < len(abbr) and abbr[a].isdigit():
                num = num * 10 + int(abbr[a])
                a += 1
            
            w += num
        
        # print(f"{a} == {len(abbr)} and {w} == {len(word)}")
        return (a == len(abbr) and w == len(word))



