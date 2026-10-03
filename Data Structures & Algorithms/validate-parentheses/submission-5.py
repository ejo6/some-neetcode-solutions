class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for char in s:
            if char in parentheses.values():
                stack.append(char)
            else:
                if len(stack) == 0: return False
                elif parentheses[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        print(stack)
        if len(stack) == 0: return True
        else: return False
