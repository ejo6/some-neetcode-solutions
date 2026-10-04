class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((temp, index))
                continue

            while len(stack) != 0 and stack[-1][0] < temp:
                result[stack[-1][1]] = index - stack[-1][1]
                stack.pop()
            stack.append((temp, index))

        return result