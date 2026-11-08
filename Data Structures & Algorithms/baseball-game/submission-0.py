class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Initialize a stack to track operation
        # x: push this score onto stack
        # +: peek 2 prev scores and push the sum
        # D: push top of stack * 2
        # C: pop off of stack
        # ---
        # Iterate through and sum (it's a list to we can do this in python)

        s = []

        for op in operations:
            match op:
                case "+":
                    s.append(s[-1] + s[-2])
                case "D":
                    s.append(s[-1] * 2)
                case "C":
                    s.pop()
                case _:
                    s.append(int(op))
        print(s)
        
        total = 0
        for score in s: total += score
        return total
        
                    